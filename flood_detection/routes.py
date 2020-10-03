from flask import render_template, url_for, flash, redirect, request, jsonify
from flood_detection import app
import json, os

@app.route("/")
@app.route("/home")
def home():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "data.json")
    json_data = json.load(open(json_url))
   
    return render_template('home.html',json_data = json_data)
