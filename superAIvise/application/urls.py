from django.urls import path
from django.http import StreamingHttpResponse
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('monitor/', lambda r: StreamingHttpResponse(gen(VideoCamera()),
                                                     content_type='multipart/x-mixed-replace; boundary=frame')),
]
