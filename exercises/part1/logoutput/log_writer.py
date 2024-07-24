from util import log_output
import time

if __name__ == "__main__":
    while True:
      with open("logs/data", "a") as log_file:
          timestamp = log_output()
          log_file.write(f"{timestamp}\n")
      time.sleep(5)