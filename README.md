# YOLOv8 Object Detection with Flask
## Description
This repository contains code for a computer vision project that utilizes YOLOv8 for object detection. The project includes Flask-based APIs for performing object detection on images using pre-trained YOLOv8 models.

## Folder Structure
dataset: Contains test data and a data.yaml file.
app.py: File containing the Flask code for the web application.
utils/predict.py: Python script containing the object detection code.
utils/train.py: Python script for training image detection using YOLOv8 architecture.
routes/obdet.py: Python script containing the API endpoint for object detection using utils/predict.py.
detect: Folder containing the YOLOv8 model weights.
## Dataset
The dataset used in this project was exported via roboflow.com. It includes 137 images annotated in YOLOv8 format. The dataset preprocessing includes auto-orientation, resizing to 640x640, and various augmentations such as rotations, random cropping, brightness adjustments, and exposure adjustments.

## Dataset Details:
Images: 137
Annotated Classes: AC, Fan, Generator, Meter, Pump

## Usage details:
Run the Flask app: python app.py

Image File:
Source: The image file is typically uploaded by the user through the web interface or provided as input to the API endpoint.
Format: Common image formats such as JPEG, PNG, or other compatible formats are supported.
Method (Flask Web Interface): Users can upload an image through the provided web interface by selecting a file using the "Choose File" button.
Method (API Endpoint): Users can send a POST request to the /object_detection API endpoint, providing the image file as a part of the request.
Sample Usage (Flask Web Interface):
Visit http://localhost:5000/object_detection to access the application.
Click on the "Choose File" button.
Select an image file from your local system.
Click on the "Submit" or "Predict" button to trigger object detection.

## Output
The object detection system generates annotated images as output, highlighting identified objects in the input image. The annotations include bounding boxes around detected objects and labels indicating the class of each object.

## Notes:
The YOLOv8 model is loaded using the provided model weights (./detect/train4/weights/best.pt).
The predict_objects function is responsible for performing object detection on the input image.
A confidence threshold is applied (if prob >= 0.50) to filter out low-confidence predictions.
The annotated image is saved in the uploads folder as annotated_image.jpg.
The API response includes details about the detected objects and the path to the annotated image.

## Example Output:
Annotated Image

In the example above, the green bounding boxes represent detected objects, and the corresponding labels indicate the object classes. The level of confidence for each detection is also displayed.

The API response includes a JSON format with details about the detected objects and the path to the annotated image, providing a comprehensive summary of the object detection results.

## Contributing
Contributions are welcome! Please follow the Contribution Guidelines for more details.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
YOLOv8: https://github.com/ultralytics/yolov8
Roboflow: https://roboflow.com/
## Contact
For questions or inquiries, please contact shlesha.pandey9@gmail.com
