import cv2


FRONTAL_FACE = "haarcascade_frontalface_default.xml"
IMAGE_NAME = "image-sm.jpeg"

faces_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + FRONTAL_FACE)
# print(faces_cascade)


def main(cap):
    frames_count = 0
    faces = []

    while True:
        success, img = cap.read()

        if not success:
            print("could not read frame")
            break

        frames_count += 1
        if frames_count % 3 == 0:
            faces = faces_cascade.detectMultiScale(img)

        for (x, y, w, h) in faces:
            # i = frames_count % 40
            i = 1
            pt1 = (x, y)
            pt2 = (x + w, y + h)
            B = (i * 10 + int(x) * i) % 255
            G = (i * 25 + int(y) * i) % 255
            color = (B, G, 255)
            thickness = 2

            cv2.rectangle(img, pt1, pt2, color, thickness)

        cv2.imshow("Video with face", img)
        key = cv2.waitKey(1)
        if key == 27:
            print("exit by esc")
            break

    cv2.destroyWindow("Video with face")


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    try:
        main(cap)
    finally:
        cap.release()

    cv2.destroyAllWindows()
