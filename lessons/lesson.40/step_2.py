import cv2

f_name = "data/image-sm.jpg"
image = cv2.imread(f_name)

# ~Red Green Blue~
#  Blue Green Red
image_gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY,
)

cv2.imshow("gray people", image_gray)
cv2.waitKey(0)
