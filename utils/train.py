
from ultralytics import YOLO
# Create a new YOLO model from scratch
model = YOLO('yolov8l.yaml')

# Load a pretrained YOLO model
model = YOLO('yolov8l.pt')

# Train the model using the Equipment-dataset for 3 epochs
yaml_filepath = './EquipmentDetection_2-1/data.yaml'
results = model.train(data= yaml_filepath, epochs=250)

meval = model.val()
print(meval.results_dict)
meval.confusion_matrix.plot()  ## confusion-matrix plot saved after running this
# Export the model to ONNX format
success = model.export(format='onnx')