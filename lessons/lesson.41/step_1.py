import cv2 as cv


def show(image):
    cv.imshow("image preview", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


def main():

    filename = "data/image-sm.jpg"
    image = cv.imread(filename)
    # show(image)

    print(image)
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.nbytes)

    scale = 0.5
    image_h, image_w, _ = image.shape

    dsize = (
        int(image_w * scale),
        int(image_h * scale),
    )

    image_small = cv.resize(image, dsize=dsize)
    print(image_small.shape)
    print(image_small.size)
    print(image_small.nbytes)

    cv.imwrite("data/image-people-smaller.jpg", image_small)


if __name__ == '__main__':
    main()
