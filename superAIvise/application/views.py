from django.shortcuts import render
from django.http import HttpResponse
# from .ml import object_detect
import sys
from .forms import Video_form
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import cv2
import threading
import gzip
from django.shortcuts import redirect
import atexit
import concurrent.futures





def index(request):
    if request.method == 'POST':
        form = Video_form(request.POST)
        if form.is_valid():
            dict = form.cleaned_data
            phone = dict['number']
            time_val = dict['time']
            if time_val == None:
                time_val = 10
            else:
                time_val *= 60
            # object_detect()
            return redirect(results, number=phone,time=time_val)

    else:
        form = Video_form()
        print(form)
    return render(request, 'index.html', {'form': form})

def results(request, number, time):
    x = threading.Thread(target=object_detect, args=(10,), daemon=True)
    x.start()
    if x.is_alive() is True:
        return render(request, 'results.html')
    else:
        data = 0
        return render(request, 'results.html', {'data':0})

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


cam = VideoCamera()


def gen(camera):
    while True:
        frame = cam.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_cam(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")


from twilio.rest import Client
from imageai.Detection import VideoObjectDetection
from twilio.twiml.messaging_response import MessagingResponse
import os
import cv2
from django.shortcuts import redirect

def send_message():
    try:
        client = Client("AC525a5d2a7d89ac5da3de9c44ca12fc7f", "4135fce201d22b34e7e79d23f12df784")
    except:
        print("Please use valid Twilio tokens to continue. Program exiting")
        exit()
    message = client.messages \
        .create(
             body='Person has left zone, please check on them',
             from_='+442033897567',
             to='+447876173222'
         )
    resp = MessagingResponse()


def forFrame(frame_number, output_array, output_count):
    count = 0
    for x in output_array:
        if x['name'] == 'person':
            count = 1
    if count == 0:
        print("why you leave")
        # send_message()
        sys.exit()

def object_detect(time):
    execution_path = os.getcwd()
    camera = cv2.VideoCapture(0)

    detector = VideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
    detector.loadModel()
    video_path = detector.detectObjectsFromVideo(camera_input=camera,
        output_file_path=os.path.join(execution_path, "camera_detected_video")
        , frames_per_second=20, per_frame_function=forFrame, minimum_percentage_probability=50, save_detected_video=True)
    return redirect(index)

# atexit.register(redirect(index))
