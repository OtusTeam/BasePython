import os
import sys
import cv2
import random

DATA_ROOT = "data"


def add_selection(image: cv2.Mat, bbox):
    x, y, w, h = bbox
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )
    thickness = 2
    cv2.rectangle(image, pt1, pt2, color, thickness)


# def process_image(image, bbox):
#     add_selection(image, bbox)


def get_roi_frame(video_cap):
    frame = None
    while True:
        success, frame = video_cap.read()
        if not success:
            print("capture error!!")
            break

        cv2.imshow("image", frame)
        key = cv2.waitKey(100)
        if key == 27:
            break

    cv2.destroyAllWindows()
    return frame


def process_video(video_cap) -> int:
    image = get_roi_frame(video_cap)
    if image is None:
        print("no image!")
        return 2

    target_selection_bbox = cv2.selectROI("Select object to follow", image)

    print(target_selection_bbox)

    # Kernelized Correlation Filte
    tracker = cv2.TrackerKCF_create()
    tracker.init(image, target_selection_bbox)

    history = []
    while True:
        success, frame = video_cap.read()
        if not success:
            print("capture error!!")
            return 2

        track_status, bbox = tracker.update(frame)
        if not track_status:
            print("tracking error")
            break

        add_selection(frame, bbox)

        history.append(
            tuple(map(int, bbox)),
        )

        for x, y, w, h in history:
            x_center = x + w // 2
            y_center = y + h // 2
            # pt1 = (x_center, y_center)
            # pt2 = (x_center + 1, y_center + 1)
            add_selection(frame, (x_center, y_center, 1, 1))

        cv2.imshow("image track", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    return 0


def main():
    filename = "pexels-tea-oebel-6814547.mp4"
    # filename = "pexels-maksim-goncharenok-5642523.mp4"
    filepath = os.path.join(DATA_ROOT, filename)

    # cap = cv2.VideoCapture(filepath)
    cap = cv2.VideoCapture(1)

    code = 1
    try:
        code = process_video(cap)
    finally:
        cap.release()

    cv2.destroyAllWindows()
    sys.exit(code)


if __name__ == '__main__':
    main()

