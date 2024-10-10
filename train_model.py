from ultralytics import YOLO  # type: ignore

# Load model
model = YOLO('yolov8n-cls.pt') # Yolo modeli
model.train(
    data = 'dataset', # Your dataset path
    epochs = 300, # Epochs count
    imgsz = 224 # Images size 
)
