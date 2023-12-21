import cv2

src =cv2.imread('pythonAIobj/202212008462_500.jpg', cv2.IMREAD_COLOR)
height, width, channel = src.shape
#pyrUp -> 업샘플링
dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)
#pyrDown -> 다운샘플링
dst2 = cv2.pyrDown(src)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
