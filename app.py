# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 22:03:36 2021

@author: Purav
"""


from flask import Flask,render_template
import pytesseract
import numpy as np
#import pyautogui
#import cv2
from Xlib import display, X
from PIL import Image #PIL

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict")
def predict():
    pytesseract.pytesseract.tesseract_cmd = "tesseract\\tesseract.exe"
    #img = pyautogui.screenshot(region=(10, 140, 1850, 700))
    #frame = np.array(img)
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    

    W,H = 200,200
    dsp = display.Display()
    try:
        root = dsp.screen().root
        raw = root.get_image(10, 140, 1850,700, X.ZPixmap, 0xffffffff)
        image = Image.fromstring("RGB", (W, H), raw.data, "raw", "BGRX")
    finally:
        dsp.close()
    
    
    shape = pytesseract.image_to_string(image)
    shape=[i.lower() for i in shape.split("\n") if i not in [""," ","\x0c"]]
    #print(shape)
    
    return render_template("index.html", prediction = shape[0] if len(shape)>0 else " ")

if __name__ == '__main__':
    app.run(debug=True)
