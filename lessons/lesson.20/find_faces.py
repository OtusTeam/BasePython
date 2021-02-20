import cv2


FRONTAL_FACE = "haarcascade_frontalface_default.xml"
IMAGE_NAME = "image-sm.jpeg"

faces_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + FRONTAL_FACE)
# print(faces_cascade)


def main():
    img = cv2.imread(IMAGE_NAME)

    # print(img)
    # print(img.shape)
    # cv2.imshow("Image", img)
    # cv2.waitKey(0)
    # cv2.destroyWindow("Image")

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # print(img_gray)
    # print(img_gray.shape)
    # cv2.imshow("Image gray", img_gray)
    # cv2.waitKey(0)
    # cv2.destroyWindow("Image gray")

    faces = faces_cascade.detectMultiScale(img_gray)
    # faces = faces_cascade.detectMultiScale(img)

    # print(faces)
    # print(faces.shape)

    for i, (x, y, w, h) in enumerate(faces):
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        B = (i * 10 + int(x) * i) % 255
        G = (i * 25 + int(y) * i) % 255
        color = (B, G, 255)
        thickness = 2

        cv2.rectangle(img, pt1, pt2, color, thickness)


    cv2.imshow("Image with faces", img)
    cv2.waitKey(0)
    cv2.destroyWindow("Image with faces")


if __name__ == "__main__":
    main()
    cv2.destroyAllWindows()
