import os
import random

import cv2

DATA_ROOT = './data'


def get_roi_frame(video_stream):
    while True:
        status, image = video_stream.read()
        if not status:
            raise Exception('capture error')

        cv2.imshow('image', image)
        key = cv2.waitKey(100)
        if key == 27:
            break

    cv2.destroyWindow('image')
    return image


def main(video_stream):
    image = get_roi_frame(video_stream)
    bbox = cv2.selectROI("Select", image)
    # image = get_sample()
    # bbox = get_roi_area()

    tracker = cv2.TrackerKCF_create()
    tracker.init(image, bbox)

    history = []
    while True:
        status, image = video_stream.read()
        if not status:
            print('capture error')
            return 2

        track_status, tracked_bbox = tracker.update(image)
        if not track_status:
            print('tracking error')
            cv2.waitKey(0)
            break

        x, y, w, h = tracked_bbox
        pt_1 = (x, y)
        pt_2 = (x + w, y + h)
        color = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))
        thickness = 2
        cv2.rectangle(image, pt_1, pt_2, color, thickness)
        history.append(tracked_bbox)

        for x, y, w, h in history:
            x_center = x + w // 2
            y_center = y + h // 2
            pt_1 = (x_center, y_center)
            pt_2 = (x_center + 3, y_center + 3)
            color = (random.randint(0, 255),
                     random.randint(0, 255),
                     random.randint(0, 255))
            thickness = 3
            cv2.rectangle(image, pt_1, pt_2, color, thickness)

        cv2.imshow('image', image)
        key = cv2.waitKey(1)
        if key == 27:
            break

    return 0


if __name__ == '__main__':
    # cap = cv2.VideoCapture(0)
    # https://www.pexels.com/search/videos/face/
    # f_name = 'production ID_5008841.mp4'
    # f_name = 'production ID_5008925.mp4'
    # f_name = 'pexels-tea-oebel-6814547.mp4'
    f_name = 'pexels-maksim-goncharenok-5642523.mp4'
    cap = cv2.VideoCapture(os.path.join(DATA_ROOT, f_name))

    code = 1
    try:
        code = main(cap)
    finally:
        cap.release()

    cv2.destroyAllWindows()
    exit(code)
