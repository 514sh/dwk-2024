from datetime import datetime, timezone, timedelta
from hashlib import sha1
import random
import time
import sys
from flask import Flask, jsonify
import os
from util import log_output


app = Flask(__name__)

@app.route("/")
def log():
    log_str = log_output()
    try:
        with open("logs/pingpong") as pingpong_log:
            for line in pingpong_log:
                pingpong_count = line
    except FileNotFoundError as e:
        pingpong_count = 0
    log_str += f"<br/> ping/pongs: {pingpong_count}"
    return log_str

@app.route("/logs")
def all_logs():
    show_logs = ""
    with open("logs/data") as log_file:
        for line in log_file:
            show_logs += line[:-1] + "<br/>"
    return show_logs

if __name__ == "__main__":
    port  = os.environ.get('PORT', 5000)
    app.run(host="0.0.0.0", port=int(port))
    
