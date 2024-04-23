import cv2 as cv


def main():
    image_filepath = "data/image-sm.jpg"
    img = cv.imread(image_filepath)

    print(img)
    print(type(img))
    print(img.shape)
    print(img.size)
    print(img.nbytes)


if __name__ == "__main__":
    main()
