import cv2


FRONTAL_FACE = "haarcascade_frontalface_default.xml"
IMAGE_NAME = "image-sm.jpeg"

faces_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + FRONTAL_FACE)
# print(faces_cascade)


def main(cap):
    while True:
        success, img = cap.read()

        if not success:
            print("could not read frame")
            break

        cv2.imshow("Choose frame", img)
        key = cv2.waitKey(1)
        if key == 27:
            print("exit by esc")
            break

    cv2.destroyWindow("Choose frame")

    bbox = cv2.selectROI("Select", img)
    print(bbox)

    tracker = cv2.TrackerKCF_create()
    ok = tracker.init(img, bbox)

    print("Init tracker ok:", ok)

    history = []
    frame_count = 0

    while True:
        success, img = cap.read()

        if not success:
            print("could not read frame")
            break

        frame_count += 1
        ok, (x, y, w, h) = tracker.update(img)

        if ok:

            # if frame_count % 3 == 0:
            history.append((int(x), int(y), int(w), int(h)))

            i = frame_count
            pt1 = (x, y)
            pt2 = (x + w, y + h)
            B = (i * 10 + int(x) * i) % 255
            G = (i * 25 + int(y) * i) % 255
            color = (B, G, 255)
            thickness = 2

            cv2.rectangle(img, pt1, pt2, color, thickness)

        for (x, y, w, h) in history:
            w_center = w // 2
            h_center = h // 2
            pt1 = (x + w_center, y + h_center)
            pt2 = (x + w_center + 1, y + h_center + 1)
            B = int(x * w) % 255
            G = int(y * h) % 255
            color = (B, G, 255)
            thickness = 2
            cv2.rectangle(img, pt1, pt2, color, thickness)

        cv2.imshow("Tracking obj", img)

        key = cv2.waitKey(1)
        if key == 27:
            print("exit by esc")
            break

    cv2.destroyWindow("Tracking obj")


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    try:
        main(cap)
    finally:
        cap.release()

    cv2.destroyAllWindows()
