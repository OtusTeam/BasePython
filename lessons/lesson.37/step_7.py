import os
import random

import cv2

CASCADE = 'haarcascade_frontalface_default.xml'

face_finder = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades,
                                                 CASCADE))


def image_proceed(image):
    # scale = .25
    scale = .5
    # scale = 1
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
    while True:
        status, image = video_stream.read()
        if not status:
            print('capture error')
            return 2
        image = image_proceed(image)
        cv2.imshow('image', image)
        key = cv2.waitKey(1)
        if key == 27:
            break
    return 0


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    code = 1
    try:
        code = main(cap)
    finally:
        cap.release()

    cv2.destroyAllWindows()
    exit(code)