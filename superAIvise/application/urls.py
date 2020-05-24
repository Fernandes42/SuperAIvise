from django.urls import path
from django.http import StreamingHttpResponse
# from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('monitor/<number>/<time>', views.monitor),
    path('video_feed', views.video_cam, name='video'),
    path('results', views.results, name='results'),


]
