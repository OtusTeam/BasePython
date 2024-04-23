import random
from typing import Sequence

import cv2 as cv
import numpy as np


def draw_bounding_box(
    frame: np.ndarray,
    bounding_box: Sequence[int],
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


def get_frame_for_roi(cap: cv.VideoCapture) -> np.ndarray | None:
    while True:
        success, frame = cap.read()
        if not success:
            print("video read error")
            return

        cv.imshow("press p to pause", frame)
        key = cv.waitKey(1)
        if key == ord("q") or key == ord("Q"):
            print("bye bye!")
            return

        if key == ord("p"):
            break

    cv.destroyAllWindows()
    return frame


def get_tracker_for_roi(cap: cv.VideoCapture) -> cv.TrackerKCF | None:
    frame_for_roi = get_frame_for_roi(cap)
    if frame_for_roi is None:
        print("video read error. no frame for roi")
        return

    target_selection_box = cv.selectROI(
        "Select region (click and pull)",
        frame_for_roi,
    )
    cv.destroyAllWindows()
    tracker = cv.TrackerKCF.create()
    tracker.init(
        image=frame_for_roi,
        boundingBox=target_selection_box,
    )
    return tracker


def track_and_show(cap: cv.VideoCapture, tracker: cv.TrackerKCF) -> None:
    while True:
        success, frame = cap.read()
        if not success:
            print("video read error. cannot track.")
            return

        track_success, bbox = tracker.update(frame)
        if not track_success:
            print("track error.")
            return

        draw_bounding_box(frame, bbox)
        cv.imshow("img with tracked object", frame)
        key = cv.waitKey(1)
        if key == ord("q") or key == ord("Q"):
            print("bye!")
            return


def process_video(cap: cv.VideoCapture):
    tracker = get_tracker_for_roi(cap)
    if tracker is None:
        print("no tracker")
        return

    track_and_show(cap, tracker)


def main():
    filename = "data/pexels-maksim-goncharenok-5642523.mp4"
    # filename = "data/pexels-tea-oebel-6814547.mp4"
    cap = cv.VideoCapture(filename)
    if not cap.isOpened():
        print("Unable to open video stream or file")
        return
    process_video(cap)


if __name__ == "__main__":
    main()
