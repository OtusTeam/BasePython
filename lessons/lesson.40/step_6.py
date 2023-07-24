import os
import random

from pathlib import Path

import cv2

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
filename = "pexels-tea-oebel-6814547.mp4"
# filename = "pexels-maksim-goncharenok-5642523.mp4"
video_file_path = DATA_DIR / filename

CASCADE = "haarcascade_frontalcatface_extended.xml"

cascade_path = os.path.join(
    cv2.data.haarcascades,
    CASCADE,
)

detector = cv2.CascadeClassifier(cascade_path)


def add_rects_to_frame(image, bboxes):
    for x, y, w, h in bboxes:
        pt_1 = (x, y)
        pt_2 = (x + w, y + h)
        # color = (127, 127, 127)
        color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )
        thickness = 3
        cv2.rectangle(
            image,
            pt1=pt_1,
            pt2=pt_2,
            color=color,
            thickness=thickness,
        )


def process_frame(frame):
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    scale_factor = 1.6
    min_neighbors = 2
    bboxes = detector.detectMultiScale(
        img_gray,
        scaleFactor=scale_factor,
        minNeighbors=min_neighbors,
        minSize=(70, 70),
    )
    add_rects_to_frame(frame, bboxes)


def process_video(video):
    while True:
        success, frame = video.read()
        if not success:
            print("video read error")
            return

        process_frame(frame)
        cv2.imshow("face", frame)
        key = cv2.waitKey(1)
        if key == 27:
            return


def main():
    print(video_file_path)
    print(video_file_path.is_file())
    video_cap = cv2.VideoCapture(str(video_file_path))
    process_video(video_cap)


if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()
