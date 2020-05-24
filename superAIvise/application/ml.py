from twilio.rest import Client
from imageai.Detection import VideoObjectDetection
from twilio.twiml.messaging_response import MessagingResponse
import os
import cv2
from django.shortcuts import redirect
from .views import *

def send_message():
    try:
        client = Client("AC525a5d2a7d89ac5da3de9c44ca12fc7f", "4135fce201d22b34e7e79d23f12df784")
    except:
        print("Please use valid Twilio tokens to continue. Program exiting")
        exit()
    message = client.messages \
        .create(
             body='Said person has left zone',
             from_='+442033897567',
             to='+447876173222'
         )
    resp = MessagingResponse()


def forFrame(frame_number, output_array, output_count):
    print('starting')
    count = 0
    for x in output_array:
        if x['name'] == 'person':
            count = 1
    if count == 0:
        print("why you leave")
        # send_message()

def object_detect(int):
    execution_path = os.getcwd()
    camera = cv2.VideoCapture(0)

    detector = VideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
    detector.loadModel()
    video_path = detector.detectObjectsFromVideo(camera_input=camera,
        output_file_path=os.path.join(execution_path, "camera_detected_video")
        , frames_per_second=1, per_frame_function=forFrame, minimum_percentage_probability=50, save_detected_video=False, detection_timeout=10)
    return redirect(index)
