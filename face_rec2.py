import cv2

url = ''
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(url)

while True:
    conn, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), [255, 0, 0], 2)

    cv2.imshow('Video', frame)
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

cap.release()
