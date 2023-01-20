import os
from random import randint

import cv2

# file_name = "data/pexels-maksim-goncharenok-5642523.mp4"
file_name = "data/pexels-tea-oebel-6814547.mp4"

cascade_file_face = "haarcascade_frontalface_default.xml"
# cascade_file_face = "haarcascade_profileface.xml"
CASCADE_PATH = os.path.join(cv2.data.haarcascades, cascade_file_face)

detector = cv2.CascadeClassifier(CASCADE_PATH)


def add_boxes_for_faces(image, faces):
    if faces is not None:
        for x, y, w, h in faces:
            p1 = x, y
            p2 = x + w, y + h
            # color = (150, 50, 250)
            color = (
                randint(0, 255),
                randint(0, 255),
                randint(0, 255),
            )

            thickness = 2
            cv2.rectangle(image, p1, p2, color, thickness)


def process_frame(frame):
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    scale_factor = 1.6
    neighbours = 2

    boxes = detector.detectMultiScale(
        image_gray,
        scale_factor,
        neighbours,
        minSize=(70, 70),
    )
    add_boxes_for_faces(frame, boxes)


def process_video(video_cap):
    while True:
        success, frame = video_cap.read()
        if not success:
            return

        process_frame(frame)
        cv2.imshow("face", frame)
        key = cv2.waitKey(1)
        if key == 27:
            return


def main():
    cap = cv2.VideoCapture(file_name)

    process_video(cap)


if __name__ == "__main__":
    main()
