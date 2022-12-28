from flask import render_template, redirect, session, request, flash, Response
from flask_app import app

from flask_app.VISION.MONITOREO import vision_monitoreo

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(vision_monitoreo.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')