from django.shortcuts import render
from django.http import HttpResponse
from .ml import object_detect
from .forms import Video_form
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import cv2
import threading
import gzip
from django.shortcuts import redirect



def index(request):
    if request.method == 'POST':
        form = Video_form(request.POST)
        if form.is_valid():
            int = form.cleaned_data
            print(int)
            # object_detect()
            return redirect(monitor)

    else:
        form = Video_form()
        print(form)
    return render(request, 'index.html', {'form': form})

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

def monitor(request):
    x = threading.Thread(target=object_detect, args=(1,), daemon=True)
    x.start()
    return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
