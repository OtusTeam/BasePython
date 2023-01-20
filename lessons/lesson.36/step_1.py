"""
Annotations:
https://github.com/bschnurr/python-type-stubs/blob/add-opencv/cv2/__init__.pyi
"""
from operator import mul, add
from functools import reduce
import cv2

# map(func, collection)
# filter(func, collection)




def main():
    img = cv2.imread("data/img-cat.jpeg")

    if img is None:
        print("could not read image")
        return

    print(img.shape)
    print(reduce(mul, img.shape))
    # numbers = [1, 2, 3, 4]
    # print(reduce(mul, numbers))
    # print(sum(numbers))
    # print(reduce(add, numbers))
    print(img.nbytes)

    cv2.imshow("Cats", img)
    key = cv2.waitKey(0)
    print("exit by key", key)


if __name__ == "__main__":
    main()
