import cv2 as cv
import numpy as np
from LMS import*
import time
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

drawing=False
mode=False
points=[]
R=[]



def draw_circle(event,x,y,flags,param):
    global drawing,mode
    if event==cv.EVENT_LBUTTONDOWN:
        drawing=True
    elif event==cv.EVENT_MOUSEMOVE :
        if drawing==True:
            cv.circle(img,(x,y),0,(0,0,255),-1)
            try:
                if (x,y)!=points[-1]:
                    points.append((x, y))
            except:
                points.append((x, y))
    elif event==cv.EVENT_LBUTTONUP:
        drawing=False
img=np.zeros((600,1100,3),np.uint8)
B=np.zeros((600,1100,3),np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20)&0xFF==27:
        break
#print(points)
cv.destroyAllWindows()
print("Please waiting...")

for i in range(len(points)-1):
    if distance(points[i],points[i+1])>2:
        cv.line(img,points[i],points[i+1],(0,0,255),1)

n=20
center=[]
for i in range(len(points)-n):
    p,r,x,y=LMS(points,i,n)
    #print(r)
    R.append(int(r))
    center.append((int(x),int(y)))
i=0
while(i<len(R)):
    if center[i]!=(0,0):
        cv.circle(img,center[i],int(R[i]),(255,0,0),1)
        cv.circle(img, points[int(i+n/2)], 2, (255, 255, 255), 1)
        cv.imshow('image', img)
    i+=1
    if cv.waitKey(10)&0xFF==27:
        break
cv.destroyAllWindows()
print("Please waiting...")
#print(R)
Z = np.zeros((600, 1100), np.float64)
for p in range(len(R)):
    cv.circle(B,(points[p][0],points[p][1]),5,(0,int(255*80/R[p]),0),5)
    Z[points[p][1]][points[p][0]]=1/R[p]*1000

X = np.arange(0, 600, 1)
Y = np.arange(0, 1100, 1)
#Z = np.ones((len(X), len(Y)), np.float64)
X, Y = np.meshgrid(X, Y)
Z=np.transpose(Z)
fig1 = plt.figure('Mask')
ax = Axes3D(fig1)
plt.title("Mask")
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
ax.set_xlabel('x label', color='r')
ax.set_ylabel('y label', color='g')
ax.set_zlabel('z label', color='b')
plt.show()


cv.imshow('image',img)
cv.imshow('B',B)
cv.waitKey(0)
cv.imwrite('a.png',img)
cv.destroyAllWindows()
