import cv2
from numba import jit, cuda
from imutils.video import FPS
import time


def process_img(frame):
    cv2.imshow('Video', frame)


def read_faces_from_img(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces

def show_face(faces, frame):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), [255, 0, 0], 2)
        cv2.putText(frame, "People", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 123), 2)
username = 'pyuser'
password = 'pyuser123'
user = 'admin'
# password = '5215052'
ip = '192.168.1.254'
port = 554
# url = f'rtsp://{user}:{password}@{ip}:{port}'

hall_url = f'rtsp://{username}:{password}@{ip}:{port}/cam/realmonitor?channel=5&subtype=0'
back_url = f'rtsp://{username}:{password}@{ip}:{port}/cam/realmonitor?channel=4&subtype=0'
external_right_url = f'rtsp://{username}:{password}@{ip}:{port}/cam/realmonitor?channel=3&subtype=0'
external_left_url = f'rtsp://{username}:{password}@{ip}:{port}/cam/realmonitor?channel=7&subtype=0'
frontal_left_url = f'rtsp://{username}:{password}@{ip}:{port}/cam/realmonitor?channel=1&subtype=0'
frontal_right_url = f'rtsp://{username}:{password}@{ip}:{port}/cam/realmonitor?channel=2&subtype=0'

url = external_right_url
# url = 'video1.mp4'
print(url)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cam = cv2.VideoCapture(url)

while True:
    conn, frame = cam.read()
    if not conn:
        break
    # faces = read_faces_from_img(frame)
    # show_face(faces, frame)
    process_img(frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
