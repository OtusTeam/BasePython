from pathlib import Path
from random import randint

import cv2 as cv
import numpy as np

filename = "pexels-maksim-goncharenok-5642523.mp4"
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
video_filepath = DATA_DIR / filename

CASCADE = "haarcascade_frontalface_default.xml"

cascade_path = str(
    Path(cv.data.haarcascades) / CASCADE
)



def draw_bbox(image, x, y, w, h):
    pt_1 = (x, y)
    pt_2 = (x + w, y + h)

    color = (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    )
    thickness = 3
    cv.rectangle(
        image,
        pt1=pt_1,
        pt2=pt_2,
        color=color,
        thickness=thickness,
    )

def detect_faces_and_add_rects(image):
    face_finder = cv.CascadeClassifier(cascade_path)
    image_gray = cv.cvtColor(
        image,
        cv.COLOR_BGR2GRAY,
    )
    plates = face_finder.detectMultiScale(
        image_gray,
        scaleFactor=2,
        minNeighbors=2,
        minSize=(70, 70),
    )

    if plates is None or len(plates) == 0:
        print("no faces found")
        return

    assert isinstance(plates, np.ndarray)
    # print(plates)
    # print(plates.shape)

    for e in plates:
        draw_bbox(*e)


def detect_face_on_video(cap):
    while True:
        success, frame = cap.read()
        if not success:
            print("video read error")
            return

        detect_faces_and_add_rects(frame)
        cv.imshow("face", frame)
        key = cv.waitKey(1)
        if key == ord("q"):
            print("bye")
            return


def main():
    video_cap = cv.VideoCapture(str(video_filepath))
    detect_face_on_video(video_cap)


if __name__ == "__main__":
    main()
