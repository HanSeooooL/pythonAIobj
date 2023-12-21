import cv2
src = cv2.imread('pythonAIobj/202212008462_500.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for i in range(len(contours)):
    cv2.drawContours(src, [contours[i]], -1, (0, 255, 255), 1)
    cv2.imshow('src', src)
cv2.waitKey(0)
cv2.destroyAllWindows()