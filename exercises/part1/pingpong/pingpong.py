from flask import Flask
import os

app = Flask(__name__)

counter = 0

@app.route("/pingpong")
def pingpong():
    global counter
    counter += 1
    with open("logs/pingpong", "w") as pingpong_log:
        pingpong_log.write(f"{counter}")
    return f"{counter}"

if __name__ == "__main__":
    port  = os.environ.get('PORT', 5000)
    app.run(host="0.0.0.0", port=int(port))