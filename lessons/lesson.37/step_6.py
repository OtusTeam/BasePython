import os
import random

import cv2

DATA_ROOT = 'data'
CASCADE = 'haarcascade_frontalface_default.xml'

face_finder = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades,
                                                 CASCADE))


def image_proceed(image):
    scale = .25
    _h, _w, _ = image.shape
    image = cv2.resize(image, (int(_w * scale), int(_h * scale)))

    faces = face_finder.detectMultiScale(image)
    for x, y, w, h in faces:
        pt_1 = (x, y)
        pt_2 = (x + w, y + h)
        color = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))
        thickness = 2
        cv2.rectangle(image, pt_1, pt_2, color, thickness)
    return image


def main(video_stream):
    status, image = video_stream.read()
    if not status:
        print('capture error')
        return
    image = image_proceed(image)
    cv2.imshow('image', image)
    cv2.waitKey(0)


if __name__ == '__main__':
    # cap = cv2.VideoCapture(0)
    # https://www.pexels.com/search/videos/face/
    # f_name = 'production ID_5008841.mp4'
    # f_name = 'production ID_5008925.mp4'
    # f_name = 'pexels-maksim-goncharenok-5642523.mp4'
    f_name = 'pexels-tea-oebel-6814547.mp4'
    cap = cv2.VideoCapture(os.path.join(DATA_ROOT, f_name))

    try:
        main(cap)
    finally:
        cap.release()

    cv2.destroyAllWindows()
