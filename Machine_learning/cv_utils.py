import numpy as np
import cv2
import mediapipe as mp
from ultralytics import YOLO


mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh

model_points = np.array([
    (0.0, 0.0, 0.0),             # Nose tip
    (0.0, -330.0, -65.0),        # Chin
    (-225.0, 170.0, -135.0),     # Left eye left corner
    (225.0, 170.0, -135.0),      # Right eye right corner
    (-150.0, -150.0, -125.0),    # Left Mouth corner
    (150.0, -150.0, -125.0)      # Right mouth corner
])

LANDMARKS_IDS = {
    'nose_tip': 1,
    'chin': 152,
    'left_eye_left_corner': 33,
    'right_eye_right_corner': 263,
    'left_mouth_corner': 61,
    'right_mouth_corner': 291
}

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,  # 0, 1, or 2. Higher complexity for more accuracy.
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    """
    Calculates the angle at point 'b' given three points a, b, c.
    Points are in [x, y] format.
    """
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    ba = a - b
    bc = c - b
    
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
    return np.degrees(angle)

def is_any_arm_raised(landmarks, img_height, angle_thresh=120, y_ratio=0.5):
    """
    Determines if any arm (left or right) is raised.
    
    Parameters:
    - landmarks: List of pose landmarks.
    - img_height: Height of the image in pixels.
    - angle_thresh: Maximum elbow angle to consider arm as raised.
    - y_ratio: Fraction of image height to set Y-coordinate threshold.
    
    Returns:
    - Boolean indicating if any arm is raised.
    """
    arms = ['left', 'right']
    for side in arms:
        shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value if side == 'left' else mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
        elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value if side == 'left' else mp_pose.PoseLandmark.RIGHT_ELBOW.value]
        wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value if side == 'left' else mp_pose.PoseLandmark.RIGHT_WRIST.value]
        
        if shoulder and elbow and wrist:
            angle = calculate_angle([shoulder.x, shoulder.y], [elbow.x, elbow.y], [wrist.x, wrist.y])
            wrist_y = wrist.y * img_height
            
            if angle < angle_thresh:
                return True
    return False

def detect_gestures(frame):
    results = pose.process(frame)
    gesture = False
    height, width, _ = frame.shape

    if results.pose_landmarks:
        # Check if any arm is raised
        gesture = is_any_arm_raised(results.pose_landmarks.landmark, height)
    
    return gesture

def normalize_landmarks(landmarks, width, height):
    normalized = []
    for lm in landmarks.landmark:
        x = lm.x * width
        y = lm.y * height
        normalized.append([x, y])
    return normalized

def get_2d_image_points(landmarks, frame_shape):
    image_points = []
    height, width, _ = frame_shape
    for name, idx in LANDMARKS_IDS.items():
        landmark = landmarks.landmark[idx]
        x = int(landmark.x * width)
        y = int(landmark.y * height)
        image_points.append((x, y))
    return np.array(image_points, dtype="double")

def estimate_head_pose(frame, landmarks):
    size = frame.shape
    focal_length = size[1]
    center = (size[1] / 2, size[0] / 2)
    camera_matrix = np.array([
        [focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1]
    ], dtype="double")
    dist_coeffs = np.zeros((4,1))  # Assuming no lens distortion

    if landmarks is None:
        return
    image_points = get_2d_image_points(landmarks, frame.shape)
    if image_points.shape[0] != 6:
        return
    success, rotation_vector, translation_vector = cv2.solvePnP(
        model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE
    )
    if not success:
        return
    # Convert rotation vector to rotation matrix
    rotation_matrix, _ = cv2.Rodrigues(rotation_vector)
    # Combine rotation and translation to get the full transformation matrix
    pose_matrix = cv2.hconcat((rotation_matrix, translation_vector))
    # Decompose the pose matrix to get Euler angles
    _, _, _, _, _, _, euler_angles = cv2.decomposeProjectionMatrix(pose_matrix)
    yaw = euler_angles[1][0]
    pitch = euler_angles[0][0]
    roll = euler_angles[2][0]
    return (yaw, pitch, roll)

def detect_faces_and_landmarks(frame):
    with mp_face_mesh.FaceMesh(static_image_mode=True,
                               max_num_faces=1,
                               refine_landmarks=True,
                               min_detection_confidence=0.5) as face_mesh:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0]
            return landmarks
        return None

mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh

def extract_frames(video_path, frame_interval=0.1):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(fps * frame_interval)
    frames = []
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if count % interval == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(frame)
        count += 1

    # for image in frames:  
    #     cv2.imshow("frame", image)
    #     cv2.waitKey(500)

    cap.release()
    return frames

def is_turned(pose_, yaw_threshold=30):
    yaw, pitch, roll = pose_
    if abs(yaw) < yaw_threshold:
        return False
    return True

def count_people(frame) -> int:
    # Initialize the YOLO model
    # This will automatically download the YOLOv8 model if not present
    model = YOLO('yolov8n.pt')  # 'yolov8n.pt' is the Nano version; for better accuracy, consider 'yolov8s.pt' or higher

    results = model(frame)[0]

    # Extract bounding boxes, class IDs, and confidences
    boxes = results.boxes  # Boxes object for YOLOv8
    person_count = 0

    for box in boxes:
        cls = box.cls  # Class ID
        conf = box.conf  # Confidence score

        # YOLOv8 uses class IDs as integers; '0' is typically 'person' in COCO
        if int(cls) == 0 and conf > 0.5:  # Filter for 'person' class with confidence > 0.5
            person_count += 1
    
    return person_count
