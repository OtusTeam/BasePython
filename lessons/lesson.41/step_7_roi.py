from pathlib import Path
from random import randint

import cv2
import cv2 as cv
import numpy as np

# filename = "pexels-tea-oebel-6814547.mp4"
filename = "pexels-maksim-goncharenok-5642523.mp4"

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
video_filepath = DATA_DIR / filename


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


def get_frame_for_roi(cap):
    while True:
        success, frame = cap.read()
        if not success:
            print("video read error")
            return

        cv.imshow("press p to pause", frame)
        key = cv2.waitKey(1)
        if key == ord("p"):
            break

    cv.destroyAllWindows()

    return frame


def process_video(cap):
    frame_for_roi = get_frame_for_roi(cap)
    if frame_for_roi is None:
        print("no frame for roi")
        return

    target_selection_box = cv.selectROI(
        "Select region (click and pull)",
        frame_for_roi,
    )

    tracker = cv.TrackerKCF.create()
    tracker.init(
        image=frame_for_roi,
        boundingBox=target_selection_box,
    )

    while True:
        success, frame = cap.read()
        if not success:
            print("video read error")
            return

        track_status, bbox = tracker.update(frame)
        if not track_status:
            print("track error")
            break

        draw_bbox(frame, *bbox)
        cv.imshow("track", frame)
        key = cv.waitKey(1)
        if key == ord("q"):
            print("bye")
            return


def main():
    video_cap = cv.VideoCapture(str(video_filepath))
    process_video(video_cap)


if __name__ == "__main__":
    main()
