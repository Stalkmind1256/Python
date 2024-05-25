import cv2
import numpy
from Camera import RTSPCamera

#target_color = [152, 255, 152] # Цвет в формате BGR
target_color = [229, 244, 255]

camera = RTSPCamera('http://158.58.130.148:80/mjpg/video.mjpg')
camera.start()

while True:
    frame = camera.read()
    if frame is None:
        continue

    result_frame, mask = camera.find_pixels(target_color)
    cv2.imshow('frame', frame)
    cv2.imshow('result', result_frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.stop()
cv2.destroyAllWindows()
