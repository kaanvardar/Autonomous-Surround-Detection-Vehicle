#!/usr/bin/python3

from time import sleep
from picamera2 import Picamera2, Preview
from libcamera import Transform
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(main={"size": (640, 480)},transform=Transform(hflip=1,vflip=1))
picam2.configure(preview_config)

try:
	while True:
		picam2.start_preview(Preview.QTGL)
		picam2.start()
		print("infinite till interrupt")
		sleep(100)
except KeyboardInterrupt:
		destroy()

def destroy():
	metadata = picam2.capture_file("image.jpg")
	print(metadata)
	picam2.close()


