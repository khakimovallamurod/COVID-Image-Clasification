from ultralytics import YOLO # type: ignore
import cv2

# load model
model = YOLO('runs/classify/train/weights/best.pt')

def image_clasification(image_path, output_image):
    image = cv2.imread(image_path)
    results = model(image)

    results[0].save(filename = output_image)