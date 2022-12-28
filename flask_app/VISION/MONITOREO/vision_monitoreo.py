#Import necessary libraries
from flask import Flask, render_template, Response
import cv2
#Initialize the Flask app
app = Flask(__name__)

def gen_frames():
    camera = cv2.VideoCapture(0)   
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat
