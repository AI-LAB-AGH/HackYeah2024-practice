import easyocr
import cv2
from PIL import Image
import numpy as np
import os
import time


def extract_text_easyocr(image):
    # Initialize the reader with desired languages
    reader = easyocr.Reader(['pl'])  # Add more languages if needed, e.g., ['en', 'es']
    # Perform OCR
    results = reader.readtext(image)
    # Extract and concatenate text
    text = ' '.join([result[1] for result in results])
    return text

# Example usage within video processing
def extract_captions_with_easyocr(video_path, frame_rate=1):
    vidcap = cv2.VideoCapture(video_path)
    if not vidcap.isOpened():
        print("Error: Could not open video.")
        return ""

    fps = vidcap.get(cv2.CAP_PROP_FPS)
    interval = int(fps / frame_rate) if fps > 0 else 30

    captions = []
    frame_count = 0
    reader = easyocr.Reader(['en'])  # Initialize once for efficiency

    prev_crop = None

    while True:
        success, frame = vidcap.read()
        if not success:
            break
        if frame_count % interval == 0:
            # Optionally crop to caption region
            cropped = crop_caption_region(frame, height_fraction=0.2)

            # Convert to RGB (EasyOCR expects RGB images)
            rgb_frame = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
            resized = cv2.resize(rgb_frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            # Perform OCR
            results = reader.readtext(rgb_frame)
            text = ' '.join([res[1] for res in results]).strip()
            text = text.replace('MF K C< CIRF', '')
            text = text.replace('MF KS C< CIRF', '')
            text = text.replace('MF KS K< CIRF', '')
            if text:
                if captions:
                    if text != captions[-1]:
                        captions.append(text)
                else:
                    captions.append(text)

        frame_count += 1

    vidcap.release()
    return ' '.join(captions)

# Define crop_caption_region as in previous examples
def crop_caption_region(frame, height_fraction=0.2):
    height = frame.shape[0]
    return frame[int(height * (1 - height_fraction)):, :]

# Usage
if __name__ == "__main__":
    video_path = os.path.join('data', 'videos', 'HY_2024_film_19.mp4')
    captions_text = extract_captions_with_easyocr(video_path, frame_rate=1)
    # Some add-ons present in the training set videos
    print("Extracted Captions:")
    print(captions_text)
