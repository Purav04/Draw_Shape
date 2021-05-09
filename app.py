from flask import Flask,render_template,request,json,jsonify
from PIL import Image
import pytesseract
import base64
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",prediction="")


@app.route("/predict",methods = ['GET','POST'])
def predict():
    
    data_url = request.values['url']
    offset = data_url.index(',')+1
    img_bytes = base64.b64decode(data_url[offset:])
    img = Image.open(BytesIO(img_bytes))
    
    new_image = Image.new("RGBA", img.size, "WHITE") 
    new_image.paste(img, (0, 0), img)              
    new_image.convert('RGB')
    
    pytesseract.pytesseract.tesseract_cmd = "tesseract\\tesseract.exe"
    
    shape = pytesseract.image_to_string(new_image)
    shape=[i.lower() for i in shape.split("\n") if i not in [""," ","\x0c"]]
    
    return json.dumps(shape[0] if len(shape)>0 else " ")

if __name__ == '__main__':
    app.run(debug=False)
