import cv2

file_name = "data/img-cat.jpeg"
# file_name = "data/car-plates.jpeg"
# file_name = "data/kittens.jpg"
# file_name = "data/purple.png"


def main():

    image = cv2.imread(file_name)
    if image is None:
        print("could not read image")
        return

    print(image)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(img_gray)
    print(img_gray.shape)
    cv2.imwrite("data/out/cat-gray.jpg", img_gray)
    # cv2.imshow("Cat gray", img_gray)
    # cv2.waitKey(0)
    # img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # print(img_rgb)
    # cv2.imshow("Purple-BGR2RGB", img_rgb)
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()
