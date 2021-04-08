# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 22:03:36 2021

@author: Purav
"""


from flask import Flask,render_template
from PIL import ImageGrab
import pytesseract

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict")
def predict():
    pytesseract.pytesseract.tesseract_cmd = "tesseract\\tesseract.exe"
    
    img = ImageGrab.grab()
    
    left = 10
    top = 140 
    right = 1850
    bottom = 870
    t = img.crop((left,top,right,bottom))
    
    shape = pytesseract.image_to_string(t)
    shape=[i.lower() for i in shape.split("\n") if i not in [""," ","\x0c"]]
    print(shape)
    
    return render_template("index.html", prediction = shape[0] if len(shape)>0 else " ")

if __name__ == '__main__':
    app.run(debug=False)