import math
import random
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
def check(x1,y1,x2,y2):
    if x1>100 or x1<-100 or y1>100 or y1<-100:
        return -1
    elif distance(x1,y1,x2,y2)<=3:
        return 1
    return 0
treasure_x=random.randint(-100,100)
treasure_y=random.randint(-100,100)
x=0
y=0
while 1:
    direct=input("Direction? ")
    dist=input("Distance? ")
    if dist>10:
        dist=input("Distance should be less or equal to 10,Distance? :) ")
    if direct==1:
        y+=dist
    if direct==2:
        y-=dist
    if direct==3:
        x+=dist
    if direct==4:
        x-=dist
    res=check(x,y,treasure_x,treasure_y)
    if(res==0):
        print "You are ",distance(x,y,0,0)," meters away from the center of the island"
    elif res==1:
        print "Congrats,you won!!!"
        break
    else:
        print "Congrats,you failed!!!"
        break
