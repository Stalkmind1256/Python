import cv2
import numpy as np
import threading
import datetime


class RTSPCamera:
    def __init__(self, rtsp_url):
        self.rtsp_url = rtsp_url
        self.cap = cv2.VideoCapture(self.rtsp_url)
        self.frame = None
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.get_frames)
        self.thread.start()

    def get_frames(self):
        """Поток получения кадров"""
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.frame = frame
            else:
                continue

    def read(self):
        return self.frame

    def stop(self):
        self.running = False
        if self.thread.is_alive():
            self.thread.join()

    def __del__(self):
        self.stop()

    def find_pixels(self, target_color_bgr, delta=10):
        if self.frame is None:
            return None, None
        # Конвертация из BGR в HSV
        target_color_hsv = cv2.cvtColor(np.uint8([[target_color_bgr]]), cv2.COLOR_BGR2HSV)[0][0]
        lower_bound = np.array([target_color_hsv[0] - delta, 100, 100])
        upper_bound = np.array([target_color_hsv[0] + delta, 255, 255])

        hsv_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
        result_frame = cv2.bitwise_and(self.frame, self.frame, mask=mask)

        return result_frame, mask
