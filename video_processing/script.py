import cv2

img=cv2.imread("feeling.png", 0)

resim=cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2)))
cv2.imwrite("feeling_resize.png", resim)
cv2.imshow("galaxy", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
