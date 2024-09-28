from ultralytics import YOLO

import cv2
import mediapipe as mp
import numpy as np
import os
import time

from cv_utils import *


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
            frames.append(frame)
        count += 1

    cap.release()
    return frames

def is_turned(pose, yaw_threshold=30):
    yaw, pitch, roll = pose
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

def classify_video_head_direction(video_path):
    frames = extract_frames(video_path, frame_interval=0.5)  # Adjust interval as needed
    preds = []
    for frame in frames:
        is_turned_away = None
        background_disturbance = False if count_people(frame) == 1 else True
        if not background_disturbance:
            landmarks = detect_faces_and_landmarks(frame)
            head_pose = estimate_head_pose(frame, landmarks)
            is_turned_away = is_turned(head_pose)
        print(f'Turned away: {is_turned_away}, background disturbance: {background_disturbance}')
        preds.append([background_disturbance, is_turned_away])
    return preds

video_path = os.path.join('data', 'videos', 'HY_2024_film_08.mp4')

start = time.time()
classify_video_head_direction(video_path)
print(f'Total time: {time.time() - start}')
