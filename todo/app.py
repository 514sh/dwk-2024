from flask import Flask, render_template
import os
import base64

app = Flask(__name__)

def get_image_b64():
    with open("logs/image_b64") as img_file:
        return img_file.read()

def write_img(decoded_img):
    with open("static/pic.jpg", "wb") as img_file:
        img_file.write(decoded_img)
    pass

@app.route("/")
def specify_port():
    todo_list = ["todo 1", "todo2"]
    img_file = get_image_b64()
    decoded_img = base64.standard_b64decode(img_file)
    write_img(decoded_img=decoded_img)
    return render_template("index.html", todo_list = todo_list)

if __name__ == "__main__":
    port  = os.environ.get('PORT', 5000)
    app.run(host="0.0.0.0", port=int(port), debug=True)