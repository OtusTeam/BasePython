import os
import random

from pathlib import Path

import cv2


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
filename = "pexels-tea-oebel-6814547.mp4"
# filename = "pexels-maksim-goncharenok-5642523.mp4"
video_file_path = DATA_DIR / filename

# CASCADE = "haarcascade_frontalcatface_extended.xml"
#
# cascade_path = os.path.join(
#     cv2.data.haarcascades,
#     CASCADE,
# )
#
# detector = cv2.CascadeClassifier(cascade_path)


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


def add_bbox_to_frame(image, bbox):
    x, y, w, h = bbox
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



def get_frame_for_roi(video):
    while True:
        success, frame = video.read()
        if not success:
            print("video read error (get for roi)")
            return

        cv2.imshow("face123", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cv2.destroyAllWindows()

    return frame


def show_selected_roi(target_selection_box, frame_for_roi):
    x, y, w, h = target_selection_box
    pt_1 = (x, y)
    pt_2 = (x + w, y + h)
    # color = (127, 127, 127)
    color = (
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255),
    )

    thickness = 2

    cv2.rectangle(
        frame_for_roi,
        pt1=pt_1,
        pt2=pt_2,
        color=color,
        thickness=thickness,
    )
    cv2.imshow("selected", frame_for_roi)
    cv2.waitKey(0)


def process_video(video):
    frame_for_roi = get_frame_for_roi(video)
    if frame_for_roi is None:
        print("no frame for roi")
        return

    print("open select roi")
    target_selection_box = cv2.selectROI("Select object to follow", frame_for_roi)
    print(target_selection_box)

    # show_selected_roi(target_selection_box, frame_for_roi)

    tracker = cv2.TrackerKCF.create()
    tracker.init(
        image=frame_for_roi,
        boundingBox=target_selection_box,
    )

    while True:
        success, frame = video.read()
        if not success:
            print("video read error")
            break

        track_status, bbox = tracker.update(frame)
        if not track_status:
            print("tracking error")
            break

        add_bbox_to_frame(frame, bbox)
        cv2.imshow("object track", frame)
        # process_frame(frame)
        # cv2.imshow("face", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break


def main():
    # print(video_file_path)
    # print(video_file_path.is_file())
    video_cap = cv2.VideoCapture(str(video_file_path))
    process_video(video_cap)


if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()
