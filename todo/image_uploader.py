import requests
import base64
import sys
import time

def upload_image():
    image = requests.get("https://picsum.photos/1200")
    return base64.standard_b64encode(image.content)

def write_b64_image(encoded_img):
    with open("logs/image_b64", "w") as img_file:
        img_file.write(encoded_img.decode('utf-8'))    

if __name__ == "__main__":
    while True:
        print("Uploading new image...")
        sys.stdout.flush()
        encoded_img = upload_image()
        write_b64_image(encoded_img=encoded_img)
        time.sleep(180)
        