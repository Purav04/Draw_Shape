from flask import Flask,render_template,request,json,jsonify
from PIL import Image
import pytesseract
import base64
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict",methods = ['GET','POST'])
def predict():
    # getting canvas image from js and decode it
    data_url = request.values['url']
    offset = data_url.index(',')+1
    img_bytes = base64.b64decode(data_url[offset:])
    img = Image.open(BytesIO(img_bytes))
    
    new_image = Image.new("RGBA", img.size, "WHITE") 
    new_image.paste(img, (0, 0), img)              
    new_image.convert('RGB')
    
    # start pytesseract
    pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract/tesseract.exe'
    
    # predict from canvas image
    shape = pytesseract.image_to_string(new_image)
    shape=[i.lower() for i in shape.split("\n") if i not in [""," ","\x0c"]]
    
    #return it to js
    return json.dumps(shape[0] if len(shape)>0 else " ")

if __name__ == '__main__':
    app.run(debug=False)
