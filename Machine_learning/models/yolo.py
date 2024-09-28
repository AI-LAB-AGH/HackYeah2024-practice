from ultralytics import YOLO

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
