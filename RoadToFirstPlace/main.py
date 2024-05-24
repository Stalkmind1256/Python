import cv2
from Camera import RTSPCamera

camera = RTSPCamera('http://158.58.130.148:80/mjpg/video.mjpg')
camera.start()

while True:
    frame = camera.read()
    if frame is None:
        continue

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.stop()
cv2.destroyAllWindows()
