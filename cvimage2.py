import cv2

src = cv2.imread('pythonAIobj/202212008462_500.jpg', cv2.IMREAD_COLOR)
height, width, channel = src.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 2)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()