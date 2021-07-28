import time
from webserver import app
from utils.numpy_to_img import numpy_to_img
from websocket import create_connection
import cv2 as cv
import os


def start():
    # Communicate with the webserver
    ws = create_connection(f"ws://127.0.0.1:5000/video_in")

    img = cv.imread("images/airplane.jpg")

    # print(numpy_to_img(img))
    time.sleep(1)

    ws.send(b"2")

    ws.send(numpy_to_img(img))

    print("Got here")

    ws.close()
