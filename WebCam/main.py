import cv2
from Camera import RTSPCamera
import datetime
import threading

#Камеры в разных потоках, в одной timelive, в другой нарисовать треугольник, который чтолибо выделяет
#target_color = [152, 255, 152] # Цвет в формате BGR
target_color = [229, 244, 255]

def camera1_thread():
    while True:
        frame = camera1.read()
        if frame is None:
            continue
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cv2.putText(frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        result_frame, mask = camera1.find_pixels(target_color)
        cv2.imshow('frame', frame)
        cv2.imshow('result', result_frame)
        cv2.imshow('mask', mask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera1.stop()

def camera2_thread():
    while True:
        _, frame2 = camera2.read()
        if frame2 is None:
            continue
        gray = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 0, 255), 2)

        #topLeft = (30,130)
        #botRight = (130,230)
        #cv2.rectangle(frame2,topLeft,botRight,(255,0,0),3)
        cv2.imshow('Camera 2',frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera2.stop()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


camera1 = RTSPCamera('http://158.58.130.148:80/mjpg/video.mjpg')
#camera2 = RTSPCamera('http://158.58.130.148:80/mjpg/video.mjpg')
camera2 = cv2.VideoCapture(0)

camera1.start()
#camera2.start()

thread1 = threading.Thread(target=camera1_thread)
#thread2 = threading.Thread(target=camera2_thread)
thread1.start()
#thread2.start()

thread1.join()
#thread2.join()

cv2.destroyAllWindows()
