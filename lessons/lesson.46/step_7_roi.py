import os.path
import random
from typing import Sequence

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
    bounding_box: Sequence[int],
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


def get_frame_for_roi(
    cap: cv.VideoCapture,
) -> np.ndarray | None:
    while True:
        success, frame = cap.read()
        if not success:
            print("video read error (or end)")
            return

        cv.imshow("press p to pause", frame)
        cv.waitKey(1)
        key = cv.waitKey(1)

        if key == ord("q") or key == ord("Q"):
            print("bye!")
            return

        if key == ord("p"):
            break

    cv.destroyAllWindows()
    return frame


def get_tracker_for_roi(
    cap: cv.VideoCapture,
) -> cv.TrackerKCF | None:
    frame_for_roi = get_frame_for_roi(cap)

    if frame_for_roi is None:
        print("didn't get frame for roi")
        return

    target_selection_bbox = cv.selectROI(
        "Select region of interest (click and pull)",
        frame_for_roi,
    )
    cv.destroyAllWindows()
    tracker = cv.TrackerKCF.create()
    tracker.init(
        image=frame_for_roi,
        boundingBox=target_selection_bbox,
    )
    return tracker


def track_and_show(
    cap: cv.VideoCapture,
    tracker: cv.TrackerKCF,
) -> None:
    while True:
        success, frame = cap.read()
        if not success:
            print("video read error (or end)")
            return

        track_success, bbox = tracker.update(frame)
        if not track_success:
            print("tracker error")
            return

        draw_bounding_box(frame, bbox)
        cv.imshow("Framed tracked img", frame)
        key = cv.waitKey(1)
        if key == ord("q") or key == ord("Q"):
            print("bye!")
            return


def run_video_with_tracker(
    cap: cv.VideoCapture,
) -> None:
    tracker = get_tracker_for_roi(cap)
    if tracker is None:
        print("no tracker error")
        return
    track_and_show(cap, tracker)


def main():
    filename = "data/pexels-tea-oebel-6814547.mp4"
    # filename = "data/pexels-maksim-goncharenok-5642523.mp4"
    cap = cv.VideoCapture(filename)
    if not cap.isOpened():
        print("Unable to open video file")
        return
    try:
        run_video_with_tracker(cap)
    except KeyboardInterrupt:
        print("bye bye!")


if __name__ == "__main__":
    main()
