import cv2 as cv


def main():
    filename = "data/image-sm.jpg"
    image = cv.imread(filename)
    # ~Red Green Blue~
    # Blue Green Red
    print(image)
    print(image.shape)
    print(image.size)
    print(image.dtype)
    image_gray = cv.cvtColor(
        image,
        cv.COLOR_BGR2GRAY,
    )
    print(image_gray)
    print(image_gray.shape)
    print(image_gray.size)

    cv.imwrite("data/image-people-gray.jpg", image_gray)
    # cv.imwrite("data/image-people-gray-invalid-rgb.jpg", image_gray)
    # show(image_gray)


if __name__ == '__main__':
    main()
