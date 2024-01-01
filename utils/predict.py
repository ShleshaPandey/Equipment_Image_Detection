from flask import Flask, request, jsonify
import cv2
import requests
import numpy as np 
from ultralytics import YOLO
import base64

# ual path to your model config fileFunction to perform object detection on an image
def predict_objects(image_path):
    model = YOLO('./detect/train4/weights/best.pt') 
    image = cv2.imread(image_path)
    results = model(image)
    print("1")

    # Extract bounding box information from the model's results
    result = results[0]
    output = []
    for box in result.boxes:
        x1, y1, x2, y2 = [round(x) for x in box.xyxy[0].tolist()]
        class_id = box.cls[0].item()
        prob = round(box.conf[0].item(), 2)
        if prob >=0.50:
            output.append([x1, y1, x2, y2, result.names[class_id], prob])
    print("11")
    # Draw bounding boxes on the image
    for box in output:
        x1, y1, x2, y2, class_name, prob = box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{class_name}:{prob}"
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    print("111")
    
    #cv2.imshow('Object Detection Result', image) 
    annotated_image_path = 'uploads/annotated_image.jpg'
    cv2.imwrite(annotated_image_path, image)  
    return output, annotated_image_path
