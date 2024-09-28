import cv2
import mediapipe as mp
import numpy as np
import os
import time

from cv_utils import *


def detect_vision_anomalies(video_path, frame_interval=1.0):
    frames = extract_frames(video_path, frame_interval=frame_interval)  # Adjust interval as needed
    preds = []
    for frame in frames:
        is_turned_away = None
        background_disturbance = False if count_people(frame) == 1 else True
        gesture = None
        if not background_disturbance:
            landmarks = detect_faces_and_landmarks(frame)
            head_pose = estimate_head_pose(frame, landmarks)
            is_turned_away = is_turned(head_pose)
            gesture = detect_gestures(frame)
        print(f'Turned away: {is_turned_away}, background disturbance: {background_disturbance}, gesture: {gesture}')
        preds.append([background_disturbance, is_turned_away, gesture])
    return preds

def get_vision_anomaly_timestamps(video_path, frame_interval=0.5):
    preds = detect_vision_anomalies(video_path, frame_interval)

    anomalies = []

    # extracting timestamps
    for anomaly_type in preds:
        timestamps = []
        for i in range(len(anomaly_type)):
            if anomaly_type[i] == None:
                continue
            if anomaly_type[i] == True:
                if len(timestamps) == 0 or len(timestamps[-1]) == 2:
                    timestamps.append()

        anomalies.append(timestamps)


video_path = os.path.join('data', 'videos', 'HY_2024_film_19.mp4')

start = time.time()
pred = detect_vision_anomalies(video_path)
print(pred)
print(f'Total time: {time.time() - start}')
