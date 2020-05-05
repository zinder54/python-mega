import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    resim = cv2.resize(img, (100,100))
    cv2.imshow("hi",resim)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized"+image,resim)
