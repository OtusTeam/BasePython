import cv2 as cv


def main():
    # image_filepath = "data/image-sm.jpg"
    image_filepath = "data/img-cat.jpeg"
    img = cv.imread(image_filepath)
    # cv.imshow("Original Image", img)
    # img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    print(img.shape)
    print(img.size)
    print(img.nbytes)
    # print(img)

    print(img_gray.shape)
    print(img_gray.size)
    print(img_gray.nbytes)
    # print(img_gray)

    cv.imwrite("data/img-cat-gray.jpeg", img_gray)


if __name__ == "__main__":
    main()
