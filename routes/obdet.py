from flask import *
from flask import request, jsonify
import cv2
import requests
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import numpy as np
from PIL import Image
from io import BytesIO
import sys
import os
import base64
sys.path.append('./utils') 
import predict
from predict import *
Upload_Folder = './uploads'

#app.config['Upload_Folder'] = Upload_Folder

from . import routes
@routes.route("/object_detection", methods=['POST'])

#tag_name = request.get_json(force=True)
#query =tag_name['Quest'] 

#def allowed_file(filename):
#    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'} 
#    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
# Load the YOLO model and other necessary configurations

# Replace with the act

def predict():
    try:
        # Receive the image file from the request
        image_file = request.files['file']
        print('')
        print("2")
        # Save the image to a temporary file
        image_path = 'uploads/temp_image.jpg'
        image_file.save(image_path)
        print("22")
        # Perform object detection
        output, annotated_image_path = predict_objects(image_path)
        print("222")
        # Convert PIL image to bytes for response
        #image_bytes = BytesIO()
        ##pil_image.save(image_bytes, format='JPEG')
        #image_bytes = image_bytes.getvalue()
    
        # Prepare the API response
        response_data = {'predictions': output, 'Annotated-Imagepath': annotated_image_path}
        print("2222")
        # Encode the image to Base64
        
        return jsonify(response_data) 
        #return(image_path)
    except Exception as e:
        print("3")
        return jsonify({'error': str(e)}), 500
 