import cv2

file_name = "data/img-cat.jpeg"
image = cv2.imread(file_name)

# print(image)
# image_converted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_converted = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image_converted.shape)
print(image_converted)

cv2.imwrite("data/img-cat-converted.jpeg", image_converted)

"haarcascade_russian_plate_number.xml"
"haarcascade_frontalcatface.xml"
"haarcascade_frontalface_default.xml"
