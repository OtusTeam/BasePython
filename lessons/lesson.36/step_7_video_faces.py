import os
import sys
import cv2
import random

DATA_ROOT = "data"
FRONTALFACE_CASCADE = "haarcascade_frontalface_default.xml"
# FRONTALFACE_CASCADE = "haarcascade_frontalface_alt_tree.xml"


detector = cv2.CascadeClassifier(
    os.path.join(
        cv2.data.haarcascades,
        FRONTALFACE_CASCADE,
    ))


def show_frame(video_cap):
    success, image = video_cap.read()
    if not success:
        print("capture error!!")
        return

    cv2.imshow("frame", image)
    cv2.waitKey(0)


def detect_faces(image: cv2.Mat):
    faces: cv2.Mat = detector.detectMultiScale(image)

    for x, y, w, h in faces:
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        thickness = 2
        cv2.rectangle(image, pt1, pt2, color, thickness)


def process_image(image):
    detect_faces(image)


def process_video(video_cap) -> int:
    while True:
        success, frame = video_cap.read()
        if not success:
            print("capture error!!")
            return 2

        process_image(frame)
        cv2.imshow("image with face", frame)

        key = cv2.waitKey(0)
        if key == 27:
            break

    return 0


def process_frame(video_cap):
    success, frame = video_cap.read()
    if not success:
        print("capture error!!")
        return

    process_image(frame)



def main():
    filename = "pexels-tea-oebel-6814547.mp4"
    filepath = os.path.join(DATA_ROOT, filename)

    cap = cv2.VideoCapture(filepath)

    code = 1
    try:
        code = process_video(cap)
    finally:
        cap.release()

    cv2.destroyAllWindows()
    sys.exit(code)


if __name__ == '__main__':
    main()

