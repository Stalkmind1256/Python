import cv2
import threading

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