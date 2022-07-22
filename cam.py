
import cv2

cap = cv2.VideoCapture(0)
# out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc(*'MJPG'),30.0, (640,480))
i = 0
while(True):
    ret,frame = cap.read()

    if ret:
        cv2.imshow('dhd',frame)
    else:
        break
    # name = str(i)+'.jpg'
    # img = cv2.imwrite(name,frame)
    # img1 = cv2.imread(name)
    # i=i+1
    # print(img)


    # cv2.imshow("nvrjnsj",img)
    # if ret==True:
    #     a=compute(name,frame,pipeline)
    # #     cv2.imshow(name, frame)
    #     out.write(a)
    # else:
    #     break
cap.release()