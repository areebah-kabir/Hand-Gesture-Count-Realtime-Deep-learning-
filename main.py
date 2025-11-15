import cv2
import mediapipe as mp


cap=cv2.VideoCapture(0)
mphands=mp.solutions.hands
hands=mphands.Hands(max_num_hands=1)
mpdraw=mp.solutions.drawing_utils

while True:
    success,img=cap.read()

    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    res=hands.process(imgRGB)

    if res.multi_hand_landmarks:

            for handlms in res.multi_hand_landmarks:
                mpdraw.draw_landmarks(img,handlms,mphands.HAND_CONNECTIONS)

                indexy=handlms.landmark[8].y
                indexmid=handlms.landmark[6].y
                indexbase=handlms.landmark[5].y
                indexbasex=handlms.landmark[5].x

                middley=handlms.landmark[12].y
                middlemid=handlms.landmark[10].y
                middlebase=handlms.landmark[9].y

                ringy=handlms.landmark[16].y
                ringmid=handlms.landmark[14].y
                ringbase=handlms.landmark[13].y

                pinkyy=handlms.landmark[20].y
                pinkymid=handlms.landmark[18].y
                pinkybase=handlms.landmark[17].y

                thumby=handlms.landmark[4].y
                thumbmid=handlms.landmark[3].y
                thumbbase=handlms.landmark[2].y
                thumbx=handlms.landmark[4].x

                a=0

                if indexy<indexmid and indexy<indexbase:
                    a+=1

                if middley<middlemid and middley<middlebase:
                    a+=1 

                if ringy<ringmid and ringy<ringbase:
                    a+=1

                if pinkyy<pinkymid and pinkyy<pinkybase:
                    a+=1

                if abs(thumbx - indexbasex) > 0.1 and thumby < thumbbase:
                     a+=1


                cv2.putText(img,str(a),(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)





    

    cv2.imshow("Image",img)

         
    if cv2.waitKey(1) &0xFF==ord('q'):
        break
