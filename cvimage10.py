import cv2

src = cv2.imread("pythonAIobj/202212008462_500.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
dst = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 4)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()