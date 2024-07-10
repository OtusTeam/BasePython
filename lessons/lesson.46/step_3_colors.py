import cv2 as cv
import numpy as np


def main():
    colored_picture = np.array(
        # row
        [
            # columns
            [
                # pixels
                # Proof: BGR
                [0, 0, 0],
                [255, 0, 0],
                [0, 255, 0],
                [0, 0, 255],
                [255, 255, 255],
            ],
        ],
        dtype=np.uint8,
    )

    print("Original picture:")
    print(colored_picture)

    cv.imwrite("data/color-pic-rgb-raw.png", colored_picture)
    cv.imwrite("data/color-pic-rgb.jpg", colored_picture)


if __name__ == "__main__":
    main()
