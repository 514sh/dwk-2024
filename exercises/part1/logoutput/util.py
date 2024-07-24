from datetime import datetime, timezone, timedelta
from hashlib import sha1
import random

def log_output():
    date_now = datetime.now(tz=timezone(timedelta(hours=8)))
    date_format = date_now.strftime(f"%y-%m-%d %H:%M:%S.%f %Z")
    random_string = sha1(f"{random.random()}".encode('UTF-8'))
    return f"{date_format}\t{random_string.hexdigest()}"

