import os
import sys
from random import randint

import cv2

# cascade_name = "haarcascade_frontalface_default.xml"
cascade_name = "haarcascade_profileface.xml"

CASCADE_PATH = os.path.join(cv2.data.haarcascades, cascade_name)

detector = cv2.CascadeClassifier(CASCADE_PATH)


def mark_faces(faces, image):
    for x, y, w, h in faces:
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        # color = (150, 200, 100)
        color = (
            randint(0, 255),
            randint(0, 255),
            randint(0, 255),
        )
        thickness = 2
        cv2.rectangle(image, pt1, pt2, color, thickness)


def process_frame(frame):
    # image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(frame)
    mark_faces(faces, frame)


def process_video(video_cap):
    while True:
        success, frame = video_cap.read()
        if not success:
            print("capture error")
            return 2

        process_frame(frame)
        cv2.imshow("image with face", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    return 0


def main():
    # file_name = "data/pexels-tea-oebel-6814547.mp4"
    file_name = "data/pexels-maksim-goncharenok-5642523.mp4"
    # file_path = os.path.join(file_name)
    cap = cv2.VideoCapture(file_name)

    code = 1
    try:
        code = process_video(cap)
    except Exception:
        print("ooops")

    cap.release()
    sys.exit(code)


if __name__ == '__main__':
    main()
