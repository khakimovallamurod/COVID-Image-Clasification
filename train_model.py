from ultralytics import YOLO  # type: ignore

# Load model
model = YOLO('yolov8n-cls.pt')
model.train(
    data = 'dataset',
    epochs = 200, 
    imgsz = 224
)
