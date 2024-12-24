import time
import uuid
from datetime import datetime

def generate_random_string():
  return str(uuid.uuid4())

def main():
  random_string = generate_random_string()
  while True:
    timestamp = datetime.now().isoformat() + 'Z'
    print(f"{timestamp}: {random_string}")
    time.sleep(5)

if __name__ == "__main__":
  main()