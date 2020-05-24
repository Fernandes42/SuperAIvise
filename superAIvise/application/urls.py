from django.urls import path
from django.http import StreamingHttpResponse
# from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.video_cam, name='video'),
    path('results/<number>/<time>', views.results, name='results'),


]
