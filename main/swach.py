from ultralytics import YOLO
import cv2
import cvzone
import math
from  sort import *
# cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture('../videos/d.mp4')
cap.set(3,1280)
cap.set(4,720)
model=YOLO('yolo-weight/best1.pt')
# result=model('images/2.jpg',show=True)
# cv2.waitKey(0)
classNames = ['nonspitting', 'spitting']
# mask = cv2.imread("../images/maskf.png")
# tracker = Sort(max_age=20,min_hits=3,iou_threshold=0.3)
while True:
    success, img = cap.read()
    # imgRegion = cv2.bitwise_and(img, mask)
    result = model(img,stream=True)
    for r in result:
        boxes=r.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0]
            x1, y1, x2, y2=int(x1),int(y1),int(x2),int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w,h=x2-x1,y2-y1
            # bbox=int(x1),int(y1),int(w),int(h)
            # print(x1,y1,x2,y2)
            cvzone.cornerRect(img,(x1,y1,w,h))
            conf=math.ceil((box.conf[0]*100))/100
            # print(conf)
            cls=int(box.cls[0])
            currentClass=classNames[cls]
            # if currentClass=='car' and conf>0.3:
            cvzone.putTextRect(img,f"{currentClass} {conf}",(max(0,x1),max(44,y1)),scale=0.7,thickness=1)
    # tracker.update(detections)
    cv2.imshow("Image",img)
    # cv2.imshow("ImageRegion", imgRegion)
    # cv2.waitKey(0)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break