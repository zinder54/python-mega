import cv2, time, pandas as pd
from datetime import datetime

video=cv2.VideoCapture(0)

first_frame=None
status_list=[None,None]
times=[]
df=pd.DataFrame(columns=["start","end"])

while True:
    check, frame = video.read() #python takes the first frame
    status=0#checks f movement is in frame and if none ==0
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #turns first frame to grey
    gray=cv2.GaussianBlur(gray,(21,21),0)#puts a GaussianBlur onto the frame, reduce noise

    if first_frame is None:#puts frame into first_frame variable
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray) #check the difference between first frame and second
    thresh_frame=cv2.threshold(delta_frame, 30, 255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2) ##checks for contours
    (cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contours in cnts: #checks contours sizes and loops them to check each frame
        if cv2.contourArea(contours) < 1000:
            continue
        status = 1#if movement in frame change status to ==1
        (x,y,w,h)=cv2.boundingRect(contours)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),3)#adds in a rectangle around contours
    status_list.append(status) #appends status where applicable from ==0 to ==1

    if status_list[-1] ==1 and status_list[-2]==0:
        times.append(datetime.now())#if status append from ==0 to ==1 apped times with date and time
    if status_list[-1] ==0 and status_list[-2]==1:
        times.append(datetime.now())#if status change back from ==1 to ==0 append times with datetime

    cv2.imshow("colour_frame", frame)
    cv2.imshow("grey frame", gray)
    cv2.imshow("delta_frame", delta_frame)
    cv2.imshow("threshold", thresh_frame)

    key=cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(status_list)
print(times)
for item in range(0,len(times),2):
    df=df.append({"start":times[item],"end":times[item+1]}, ignore_index=True)
df.to_csv("times.csv")

video.release()
cv2.destroyAllWindows()
