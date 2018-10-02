import cv2
import time
#-*-coding:utf-8-*-
interval = 1          
num_frames = 10      
out_fps = 10           

cap = cv2.VideoCapture(0)
size =(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
       int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
video = cv2.VideoWriter(
    "time_lapse.avi", 
    cv2.VideoWriter_fourcc('M','P','4','2'), 
    out_fps, 
    size
)
for i in range(9):
    cap.read()
try:
    for i in range(num_frames):
        _, frame = cap.read()
        video.write(frame)
        print('Frame {} is captured.'.format(i))
        time.sleep(interval)
except KeyboardInterrupt:

    print('Stopped! {}/{} frames captured!'.format(i, num_frames))
video.release()
cap.release()
