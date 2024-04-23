import os.path
import random

import cv2 as cv
import numpy as np

CASCADE = "haarcascade_frontalface_default.xml"
face_cascade_path = os.path.join(
    cv.data.haarcascades,
    CASCADE,
)

face_finder = cv.CascadeClassifier(face_cascade_path)


def draw_bounding_box(
    frame: np.ndarray,
    bounding_box: tuple[int, int, int, int],
) -> None:
    thickness = 2
    x, y, w, h = bounding_box
    pt_1 = (x, y)
    pt_2 = (x + w, y + h)
    color = tuple(
        random.randint(0, 255) for _ in range(3)
    )
    cv.rectangle(
        img=frame,
        pt1=pt_1,
        pt2=pt_2,
        thickness=thickness,
        color=color,
    )


def detect_face_and_draw_bounding_boxes(frame: np.ndarray):
    image_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_finder.detectMultiScale(
        image_gray,
        scaleFactor=2,
        # minNeighbors=2,
        minSize=(70, 70),
    )
    if faces is None or len(faces) == 0:
        print("No faces found")
        return

    assert isinstance(faces, np.ndarray)
    for bbox in faces:
        draw_bounding_box(frame, bbox)


def detect_face_on_video(cap: cv.VideoCapture):
    while True:
        success, frame = cap.read()
        if not success:
            print("video read error")
            return

        detect_face_and_draw_bounding_boxes(frame)
        cv.imshow("Frame with face", frame)
        key = cv.waitKey(1)
        if key == ord("q") or key == ord("Q"):
            print("bye!")
            return


def main():
    # filename = "data/pexels-maksim-goncharenok-5642523.mp4"
    filename = "data/pexels-tea-oebel-6814547.mp4"
    cap = cv.VideoCapture(filename)
    if not cap.isOpened():
        print("Unable to open video stream or file")
        return
    detect_face_on_video(cap)


if __name__ == "__main__":
    main()
