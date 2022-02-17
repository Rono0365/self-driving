import cv2
import numpy as np
from PIL import ImageGrab
import math as m
import time
from time import sleep
from pynput.keyboard import Key, Controller
kb = Controller()
#Author:$Rono
#~"i think neuralnetworks are overrated"
start = time.time()
k2009 = ''

def roi(*n):
    vertices = np.array([[0,600],[0,300],[180,10],[320,10],[800,600],[800,600]])
    mask = np.zeros_like(img_gray)
    cv2.fillPoly(mask,[vertices],255)
    masked = cv2.bitwise_and(img_gray,mask)
    return masked
while True:#                                x1  y1  x2  y2
    screen = np.array(ImageGrab.grab(bbox=(518,342,1069,598)))
    img_gray = cv2.cvtColor(np.array(screen),cv2.COLOR_BGR2GRAY)
    carR = cv2.CascadeClassifier('cars.xml')
    vertices = np.array([[0,600],[0,400],[200,10],[600,10],[800,400],[800,600]])
    processed_img = roi(screen,vertices)
    car = carR.detectMultiScale(processed_img,1.1112,2)
    
    #screen = 
    for (x,y,w,h) in car:
        final = (time.time()-start)
        ric = cv2.rectangle(screen,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.line(ric,(300,220),(300,230),(0,0,255),7)
        
        chll = x+w
        c = w**2 + h**2
        realC = m.sqrt(c)
        CC = realC*0.02645833
        ric = cv2.rectangle(screen,(x,y),(x+w,y+h),(255,0,0),2)
        shadow_W= w*0.02645833
        realL_w = 1.65*100
        #focal_point = f=(pXd)/w 126.06060606060606
        #so dist is given by d = wXf/p
        distance = int(((realL_w*206.06060606060606)/w)/100)
        if CC > 3.5:
            cv2.rectangle(screen,(x,y),(x+w,y+h),(0,0,255),7)
            cv2.putText(ric,"SLowdown ", (x+w,x), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255, 255), 5)
            print(":slowing down")
            kb.press(Key.down)
            kb.press(Key.down)
            kb.press(Key.down)
            kb.press(Key.right)
            sleep(0.08)
            kb.release(Key.down)
            kb.release(Key.right)
            #cv2.putText(ric,"{}".format(distance), (x,y), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255, 255), 5)
            
        
        A = int((((x+w)+x)/2))
        B = int((((y+h)+y)/2))
        minus_a,minus_b = 410 - A,364 - B
        fhypotenus = minus_b**2+minus_a**2
        virtual_d = m.sqrt(fhypotenus)
        dist = ((realL_w*shadow_W)/virtual_d)/100
        #car_width = cv2.line(ric,(x,y),(x+w,y+h),(0,0,255),2)
        A1,A2 = x+w-x,y+h-y
        #car_width
        A3 = A1**2+A2**2
        A4 =m.sqrt(A3)
        A5 = A4
        A6 = 180/A5#scale factor of car in real time
        s_dist = (virtual_d*0.0264583333) #on screen
        s_dist1 = (s_dist)*A6
        start = time.time()
        if final > 0:
            final2 = s_dist1/final
        # speed + "{}kph CW {}".format(int((final*100)+ 10),realC*0.02645833)
        cv2.putText(ric,"Dist {}mtrs".format(distance), (x,y), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0, 255), 2)
        cv2.putText(ric,"{}".format("Middle"), (794,100), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0, 255), 2)
        
        #increase in speed
        #reduce speed or stop
        speed = "speed@"
        #print(current)
        #now detemining the speed s=D/T
        #"prolly another day"
        #left and right determination
        #important points to note (725,794,862) all Xs
        cv2.line(ric,(300,220),(int((((x+w)+x)/2)),int((((y+h)+y)/2))),(0,0,255),2)
         
        
        cv2.rectangle(screen,(300,200),(320,220),(25,0,255),1)
        cv2.rectangle(screen,(280,200),(300,220),(255,0,255),1)#purple
        #cv2.rectangle(screen,(320,200),(340,220),(25,0,255),1)
        Gm1 = (int((((y+h)+y)/2))/220)/(int((((x+w)+x)/2))/300)
        #cv2.putText(screen,"{}".format(k2009), ((int(((, cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0, 255), 2)
        #0.4 = centre//here you need to first slowdown or turn right or left
        #Gm1>0.4#turn right
        hey = ""
        cv2.putText(ric,"{}".format(hey), (200,200), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0, 255), 2)
        """if Gm1 > 0.49 and Gm1 < 1:
            hey.join(":slowdown & turn right")
            print(":slow down & turn right")
            sleep(0.08)
            kb.press(Key.right)
            kb.release(Key.right)"""
        #Gm1<0.4#turn left
        for CC in range(3,7):
            if Gm1 <= 0.1 :
                hey.join(":slowdown & turn right")
                print(Gm1)
                print(":slow down & turn right ")
                kb.press(Key.left)
                sleep(0.08)
                kb.release(Key.left)
                cv2.line(ric,(int((((x+w)+x))),int((((y+h)+y)/2))),(int((((x+w)+x)/2)),int((((y+h)+y)/2))),(255,0,0),2)
       
            if Gm1 > 0.5 and Gm1 < 0.59:
                print(Gm1)
                print(":slow down & turn right ")
                kb.press(Key.left)
                sleep(0.08)
                kb.release(Key.left)    
            if Gm1 >  0.34 and Gm1 <0.41 :
                hey.join(":slowdown & turn left")
                print(Gm1)
                print(":slowdown & turn left")
                kb.press(Key.left)
                sleep(0.08)
                kb.release(Key.left)
               
            if Gm1 >  0.2 and Gm1 <0.34 :
                hey.join(":slowdown & turn left")
                print(Gm1)
                print(":slowdown & turn left")
                kb.press(Key.down)
                sleep(0.1)
                kb.release(Key.down)
                kb.press(Key.up)
                sleep(0.1)
                kb.release(Key.up)
            '''    
            if "0.2" in str(Gm1):
                hey.join(":slowdown & turn left")
                print(":slowdown & turn left")
                kb.press(Key.down)
                kb.press(Key.left)
                kb.press(Key.left)
                sleep(0.08)
                kb.release(Key.down)
                kb.release(Key.left)
           '''
            if Gm1 > 0.59 and Gm1 < 0.810:
                hey.join(":slowdown & turn right")
                print(":slow down & turn right ")
                kb.press(Key.right)
                sleep(0.08)
                kb.release(Key.right)
                #kb.release(Key.left)    
            #Gm1=0.4
            print(Gm1)
            for x in range(724,862):#given x1 = 518,1069
                cv2.line(ric,(724,500),(862,500),(0,0,255),2)
                #go right
                
            #virtual_dist = cv2.line(ric,(410,364),(int((((x+w)+x)/2)),int((((y+h)+y)/2))),(0,0,255),2)
            #am now getting c**
        
        
        
        
    #cv2.imshow("screen",screen)#processed_img
    cv2.imshow("Dummy.ai",screen)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
