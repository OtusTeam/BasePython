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
):
    x, y, w, h = bounding_box
    pt_1 = x, y
    pt_2 = x + w, y + h
    color = tuple(
        random.randint(0, 255)
        for _ in range(3)
    )

    thickness = 2
    cv.rectangle(
        img=frame,
        pt1=pt_1,
        pt2=pt_2,
        thickness=thickness,
        color=color,
    )


def detect_faces_and_draw_bounding_boxes(
    frame: np.ndarray,
    scale_factor: float = 1.5,
    min_size: tuple[int, int] = (70, 70),
):
    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_finder.detectMultiScale(
        img_gray,
        scaleFactor=scale_factor,
        # minNeighbors=5,
        minSize=min_size,
        # flags=cv.CASCADE_SCALE_IMAGE,
        # outputRejectLevels=True
    )

    if faces is None or len(faces) == 0:
        print("No results found")
        return

    assert isinstance(faces, np.ndarray)
    for bbox in faces:
        draw_bounding_box(frame, bbox)


def detect_face_on_video(
    cap: cv.VideoCapture,
):
    while True:
        success, frame = cap.read()
        if not success:
            print("video read error (or end)")
            return

        detect_faces_and_draw_bounding_boxes(frame)
        cv.imshow("Framed face", frame)
        key = cv.waitKey(1)
        if key == ord("q") or key == ord("Q"):
            print("bye!")
            return


def example_img_faces():
    image_filepath = "data/image-sm.jpg"
    img = cv.imread(image_filepath)
    detect_faces_and_draw_bounding_boxes(img)
    cv.imwrite("data/image-sm-faces.jpg", img)


def main():
    # filename = "data/pexels-tea-oebel-6814547.mp4"
    filename = "data/pexels-maksim-goncharenok-5642523.mp4"
    cap = cv.VideoCapture(filename)
    if not cap.isOpened():
        print("Unable to open video file")
        return
    try:
        detect_face_on_video(cap)
    except KeyboardInterrupt:
        print("bye bye!")


if __name__ == "__main__":
    main()
