import cv2

f_name = "data/image-sm.jpg"
image = cv2.imread(f_name)

print(image)
print(type(image))
print(image.shape)
print(image.nbytes)

scale = 0.5
image_h, image_w, _ = image.shape

cv2.imshow("image people", image)
# cv2.waitKey(0)

dsize = (
    # x axis
    int(image_w * scale),
    # y axis
    int(image_h * scale)
)

image_small = cv2.resize(image, dsize)
print(image_small.shape)

cv2.imshow("scaled people", image_small)
# cv2.waitKey(0)

cv2.imwrite("data/image-sm-scaled_0.5.jpg", image_small)
