import cv2 as cv
import numpy as np


def main():
    # RGB or BGR mode by default?
    colored_picture = np.array(
        [
            [
                # PROOF: BGR
                [0, 0, 0],
                [255, 0, 0],
                [0, 255, 0],
                [0, 0, 255],
                [255, 255, 255],
            ]
        ],
        dtype=np.uint8,
    )
    print("Original pic:")
    print(colored_picture)
    cv.imwrite("data/color-pic-rgb-raw.png", colored_picture)
    cv.imwrite("data/color-pic-rgb.jpg", colored_picture)

    img_gray = cv.cvtColor(colored_picture, cv.COLOR_RGB2GRAY)
    print("RGB 2 Gray pic:")
    print(img_gray)
    cv.imwrite("data/color-pic-rgb2gray.png", img_gray)

    img_gray = cv.cvtColor(colored_picture, cv.COLOR_BGR2GRAY)
    print("BGR 2 Gray pic:")
    print(img_gray)
    cv.imwrite("data/color-pic-bgr2gray.png", img_gray)


if __name__ == "__main__":
    main()
