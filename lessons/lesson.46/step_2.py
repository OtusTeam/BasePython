import cv2 as cv


def main():
    image_filepath = "data/img-cat.jpeg"
    img = cv.imread(image_filepath)

    # cv.imshow("Cat Image", img)
    # cv.waitKey(0)
    # Blue
    # Green
    # Red
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    print("shape:", img.shape)
    print("dtype:", img.dtype)
    print("size:", img.size)
    print("nbytes:", img.nbytes)

    print("gray shape:", img_gray.shape)
    print("gray dtype:", img_gray.dtype)
    print("gray size:", img_gray.size)
    print("gray nbytes:", img_gray.nbytes)
    print(img_gray[0])

    cv.imwrite("data/img-cat-gray.jpeg", img_gray)


if __name__ == "__main__":
    main()
