import cv2
# img = cv2.imread("image.jpg")
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# resized_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# gray=cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
# faces=face_cascade.detectMultiScale(
#     gray,
#     scaleFactor=1.1,
#     minNeighbors=5,
#     minSize=(30, 30)
# )
# for x,y,w,h in faces:
#     cv2.rectangle(resized_img,(x,y),(x+w,y+h),(0,0,255),3)
# cv2.imshow("Face Detection window", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow("Face Detection window", frame)
    key=cv2.waitKey(1)
    if key == ord('e'):
        break
video.release()
cv2.destroyAllWindows()