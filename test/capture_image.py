import cv2

name = "21bce7778"

cam = cv2.VideoCapture(1)

cv2.namedWindow("Press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Press space to take a photo", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Press space to take a photo", frame)
    
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        img_name = "data/" + name + "/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
cam.release()

cv2.destroyAllWindows()
        
        