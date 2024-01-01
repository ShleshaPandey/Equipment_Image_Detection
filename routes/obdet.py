from flask import *
from flask import request, jsonify
import cv2
import requests
from flask import Flask, flash, request, redirect, url_for 
from ultralytics import YOLO
import numpy as np 
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
 
def predict():
    try:
        # Receive the image file from the request
        image_file = request.files['file']
        print('')
        print("2")
        # Save the image to a temporary file
        image_path = 'uploads/temp_image.jpg'
        image_file.save(image_path) 
        # Perform object detection
        output, annotated_image_path = predict_objects(image_path)   
        # Prepare the API response
        response_data = {'predictions': output, 'Annotated-Imagepath': annotated_image_path} 
        # Encode the image to Base64
        
        return jsonify(response_data) 
        #return(image_path)
    except Exception as e: 
        return jsonify({'error': str(e)}), 500
 
