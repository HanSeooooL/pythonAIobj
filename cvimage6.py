import cv2
src = cv2.imread("pythonAIobj/202212008462_500.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, mid = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
dst = cv2.blur(mid, (10,10), anchor=(-1,-1), borderType=cv2.BORDER_DEFAULT)
cv2.imshow('mid', mid)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()