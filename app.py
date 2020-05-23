# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot
# from twilio.rest import Client
# from imageai.Detection import VideoObjectDetection
# from twilio.twiml.messaging_response import MessagingResponse
# import os
# import cv2
#
# def window():
#     app = QApplication(sys.argv)
#     widget = QWidget()
#
#     button1 = QPushButton(widget)
#     button1.setText("Button1")
#     button1.move(64,32)
#     button1.clicked.connect(button1_clicked)
#
#     button2 = QPushButton(widget)
#     button2.setText("Button2")
#     button2.move(64,64)
#     button2.clicked.connect(button2_clicked)
#
#     widget.setGeometry(250,150,1200,800)
#     widget.setWindowTitle("PyQt5 Button Click Example")
#     widget.show()
#     sys.exit(app.exec_())
#
#
# def button1_clicked():
#     object_detect()
#
#
# def button2_clicked():
#     print("Button 2 clicked")
#
# def send_message():
#     try:
#         client = Client("AC525a5d2a7d89ac5da3de9c44ca12fc7f", "4135fce201d22b34e7e79d23f12df784")
#     except:
#         print("Please use valid Twilio tokens to continue. Program exiting")
#         exit()
#     message = client.messages \
#         .create(
#              body='Said person has left zone',
#              from_='+442033897567',
#              to='+447876173222'
#          )
#     resp = MessagingResponse()
#
#
# def forFrame(frame_number, output_array, output_count):
#     leniancy = get_leniancy()
#     if leniancy == None:
#         leniancy = 30
#     bounds = get_bounds()
#     if bounds == None:
#         count = 0
#         for x in output_array:
#             if x['name'] == 'person':
#                 count = 1
#         if count == 0:
#             print("why you leave")
#             # send_message()
#             exit()
#     else:
#         count = 0
#         for x in output_array:
#             if x['name'] == 'person' and (x['box_points'][0] + leniancy) < bounds[0] and (x['box_points'][1] + leniancy) < bounds[1] and (x['box_points'][2] + leniancy) > bounds[2] and (x['box_points'][3] + leniancy) > bounds[3] :
#                 count = 1
#         if count == 0:
#             print("out of bounds bitch")
#             # send_message()
#             exit()
#
#
# def get_bounds():
#     # x1,y1,x2,y2
#     return None
#     return [100,100,500,500]
#
# def get_leniancy():
#     return 30
#
# def object_detect():
#     print("this is getting triggered")
#     execution_path = os.getcwd()
#     camera = cv2.VideoCapture(0)
#
#     detector = VideoObjectDetection()
#     detector.setModelTypeAsYOLOv3()
#     detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
#     detector.loadModel()
#     video_path = detector.detectObjectsFromVideo(camera_input=camera,
#         output_file_path=os.path.join(execution_path, "camera_detected_video")
#         , frames_per_second=1, per_frame_function=forFrame, minimum_percentage_probability=50, save_detected_video=False)
#     print(video_path)
#
# if __name__ == '__main__':
#    window()

import Tkinter
top = Tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()
