import cv2 as cv


def main():
    image_filepath = "data/image-sm.jpg"
    img = cv.imread(image_filepath)

    print(img)
    print(type(img))
    print("shape:", img.shape)
    print("dtype:", img.dtype)
    print("dtype:", img.dtype)
    print("size:", img.size)
    print("nbytes:", img.nbytes)


if __name__ == "__main__":
    main()
