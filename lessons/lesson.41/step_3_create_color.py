import cv2 as cv
import numpy as np


def main():
    # Proof BGR mode (by default)
    color_pic = np.array(
        [
            [
                [0, 0, 0],
                [255, 0, 0],
                [0, 255, 0],
                [0, 0, 255],
                [255, 255, 255],
            ],
        ],
        dtype=np.uint8,
    )

    print(color_pic)
    cv.imwrite("data/color-pic-rgb-raw.png", color_pic)

    color_pic_bgr = cv.cvtColor(color_pic, cv.COLOR_RGB2BGR)
    print(color_pic_bgr)
    cv.imwrite("data/color-pic-rgb2bgr.png", color_pic_bgr)


if __name__ == '__main__':
    main()
