import os
import cv2

# file_name = "data/kittens.jpg"
file_name = "data/fake_cats.jpg"
# file_name = "data/kitten.jpg"
# file_name = "data/img-cat.jpeg"

cascade_file_frontal_cat_face = "haarcascade_frontalcatface_extended.xml"
# cascade_file_frontal_cat_face = "haarcascade_frontalcatface.xml"
# cascade_file_frontal_cat_face = "haarcascade_eye.xml"
CASCADE_PATH = os.path.join(cv2.data.haarcascades, cascade_file_frontal_cat_face)

detector = cv2.CascadeClassifier(CASCADE_PATH)


def main():
    image = cv2.imread(file_name)
    if image is None:
        print("could not read image")
        return

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image_h, image_w = image.shape

    scale_factor = 1.01
    neighbours = 2
    cat_faces = detector.detectMultiScale(
        image_gray,
        scale_factor,
        neighbours,
        minSize=(100, 100),
        maxSize=(900, 900),
    )
    print(cat_faces)

    if cat_faces is not None:
        for x, y, w, h in cat_faces:
            p1 = x, y
            p2 = x + w, y + h
            color = (150, 50, 250)
            thickness = 2
            cv2.rectangle(image, p1, p2, color, thickness)

    cv2.imshow("Cats faces", image)
    cv2.waitKey(0)

    # cv2.imwrite("data/out/kittens-sm.jpg", image)


if __name__ == "__main__":
    main()
