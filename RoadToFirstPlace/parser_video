import cv2
import datetime
import threading
import os

out_folder = "folders"
if not os.path.exists(out_folder):
    os.makedirs(out_folder)

capture = cv2.VideoCapture('Videos/Смешни Котки И Котенца Мяукане 2016.mp4')

fps = capture.get(cv2.CAP_PROP_FPS)
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

frames = []

frame_count = 0
while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Добавляем кадр в список
    frames.append(frame)

    frame_count += 1
    # current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # cv2.putText(frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

print(f"Сохранено {frame_count} кадров в памяти")
print(frames)
