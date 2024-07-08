from datetime import datetime, timezone, timedelta
from hashlib import sha1
import random
import time
import sys

while True:
    date_now = datetime.now(tz=timezone(timedelta(hours=8)))
    date_format = date_now.strftime(f"%y-%m-%d %H:%M:%S.%f %Z")
    random_string = sha1(f"{random.random()}".encode('UTF-8'))
    sys.stdout.flush()
    print(f"{date_format}\t{random_string.hexdigest()}")
    time.sleep(5)
