import argparse
import requests
import time
from server import serve
from multiprocessing import Process

SERVER_URL = "http://127.0.0.1:8095/print"
SERVER_HEALTH_URL = "http://127.0.0.1:8095/health"

def server_is_running():
    try:
        response = requests.get(SERVER_HEALTH_URL)
        return True if response.status_code == 200 else False
    except requests.ConnectionError:
        return False

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description='Send images or text to the printer.')
    parser.add_argument('--image', type=str, help='Path to the image file to be printed.')
    parser.add_argument('--text', type=str, help='Text string to be printed.')
    args = parser.parse_args()

    # If the server is not running, start it
    if not server_is_running():
        # Start server in a new process
        p = Process(target=serve)
        p.start()
        time.sleep(2)  # wait for 2 seconds to ensure the server is ready

    # If image or text arguments are provided, send them as requests to the server
    if args.image or args.text:
        data = {}
        if args.image:
            with open(args.image, 'rb') as f:
                data['image'] = f.read()
        if args.text:
            data['text'] = args.text
        response = requests.post(SERVER_URL, data=data)
        print(response.text)

if __name__ == "__main__":
    main()
