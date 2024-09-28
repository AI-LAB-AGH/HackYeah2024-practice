import numpy as np
import cv2
import mediapipe as mp


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