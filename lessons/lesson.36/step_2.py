import cv2

file_name = "data/kittens.jpg"


def main():
    image = cv2.imread(file_name)
    if image is None:
        print("could not read image")
        return

    print(image.shape)
    image_h, image_w, _ = image.shape
    scale = 0.5

    target_d = int(image_w * scale), int(image_h * scale)
    image_sm = cv2.resize(image, target_d)
    print(image_sm.shape)

    cv2.imwrite("data/out/kittens-sm.jpg", image_sm)


if __name__ == "__main__":
    main()
