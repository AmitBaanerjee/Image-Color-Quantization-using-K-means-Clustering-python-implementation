import numpy as np
import cv2
np.random.seed(sum([ord(c) for c in "amitbane"]))
'''*********** K=3 **********8'''
def ed(center, x):
    s = 0; 
    for i in range(len(center)):
        s= s + ((center[i]-x[i])**2);
        result=np.sqrt(s)
    return result

def kmeans(center,x):
    c1=[]
    c2=[]
    c3=[]
    vector=[]
    for i in range(len(x)):
        temp=[]
        minimum=1000
        index=0
        for j in range(len(center)):
            l=ed(center[j],x[i])
            temp.append(l)
        for k in range(len(temp)):
            if(temp[k]<minimum):
                minimum=temp[k]
                index=k
        if(index==0):
            c1.append(x[i])
            vector.append(0)
        elif(index==1):
            c2.append(x[i])
            vector.append(1)
        else:
            c3.append(x[i])
            vector.append(2)          
    return c1,c2,c3,vector

def mean(cluster):
    cluster=np.asarray(cluster)
    x=cluster[:,[0]]
    y=cluster[:,[1]]
    z=cluster[:,[2]]
    xmean=np.mean(x)
    ymean=np.mean(y)
    zmean=np.mean(z)
    return np.round(xmean,0),np.round(ymean,0),np.round(zmean,0)

k=3
loop=18
image=cv2.imread('baboon.jpg')
nimage=np.reshape(image,(-1,3))
x=nimage[:,[0]]
y=nimage[:,[1]]
z=nimage[:,[2]]
x=x.tolist()
y=y.tolist()
z=z.tolist()

centers=[]
for i in range(k):
    temp=nimage[np.random.choice(nimage.shape[0], replace=False)]
    centers.append(temp)

for i in range(loop):
    cluster1, cluster2, cluster3, vector = kmeans(centers,nimage)
    centers[0] = mean(cluster1)
    centers[1] = mean(cluster2)
    centers[2] = mean(cluster3)

npv = np.asarray(vector)
for i in range(npv.shape[0]):
    v = npv[i]
    if(v == 0):
        nimage[i]=centers[0]
    elif(v == 1):
        nimage[i]=centers[1]
    else:
        nimage[i]=centers[2]

qimg=np.reshape(nimage,(image.shape))
cv2.imwrite('task3_baboon_3.jpg',qimg)
'''*********** K=5 ************'''
def kmeans(center,x):
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    c5=[]
    vector=[]
    for i in range(len(x)):
        temp=[]
        minimum=1000
        index=0
        for j in range(len(center)):
            l=ed(center[j],x[i])
            temp.append(l)
        for k in range(len(temp)):
            if(temp[k]<minimum):
                minimum=temp[k]
                index=k
        if(index==0):
            c1.append(x[i])
            vector.append(0)
        elif(index==1):
            c2.append(x[i])
            vector.append(1)
        elif(index==2):
            c3.append(x[i])
            vector.append(2) 
        elif(index==3):
            c4.append(x[i])
            vector.append(3)
        else:
            c5.append(x[i])
            vector.append(4)
    return c1,c2,c3,c4,c5,vector

k=5
loop=18
image=cv2.imread('baboon.jpg')
nimage=np.reshape(image,(-1,3))
x=nimage[:,[0]]
y=nimage[:,[1]]
z=nimage[:,[2]]
x=x.tolist()
y=y.tolist()
z=z.tolist()

centers=[]
for i in range(k):
    temp=nimage[np.random.choice(nimage.shape[0], replace=False)]
    centers.append(temp)

for i in range(loop):
    cluster1, cluster2, cluster3,cluster4,cluster5, vector = kmeans(centers,nimage)
    centers[0] = mean(cluster1)
    centers[1] = mean(cluster2)
    centers[2] = mean(cluster3)
    centers[3] = mean(cluster4)
    centers[4] = mean(cluster5)

npv = np.asarray(vector)
for i in range(npv.shape[0]):
    v = npv[i]
    if(v == 0):
        nimage[i]=centers[0]
    elif(v == 1):
        nimage[i]=centers[1]
    elif(v == 2):
        nimage[i]=centers[2]
    elif(v == 3):
        nimage[i]=centers[3]
    else:
        nimage[i]=centers[4]

qimg=np.reshape(nimage,(image.shape))
cv2.imwrite('task3_baboon_5.jpg',qimg)

'''******* K=10 ********'''
def kmeans(center,x):
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    c5=[]
    c6=[]
    c7=[]
    c8=[]
    c9=[]
    c10=[]
    vector=[]
    for i in range(len(x)):
        temp=[]
        minimum=1000
        index=0
        for j in range(len(center)):
            l=ed(center[j],x[i])
            temp.append(l)
        for k in range(len(temp)):
            if(temp[k]<minimum):
                minimum=temp[k]
                index=k
        if(index==0):
            c1.append(x[i])
            vector.append(0)
        elif(index==1):
            c2.append(x[i])
            vector.append(1)
        elif(index==2):
            c3.append(x[i])
            vector.append(2) 
        elif(index==3):
            c4.append(x[i])
            vector.append(3)
        elif(index==4):
            c5.append(x[i])
            vector.append(4)
        elif(index==5):
            c6.append(x[i])
            vector.append(5)
        elif(index==6):
            c7.append(x[i])
            vector.append(6)
        elif(index==7):
            c8.append(x[i])
            vector.append(7)
        elif(index==8):
            c9.append(x[i])
            vector.append(8)
        else:
            c10.append(x[i])
            vector.append(9)
    return c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,vector

k=10
loop=18
image=cv2.imread('baboon.jpg')
nimage=np.reshape(image,(-1,3))
x=nimage[:,[0]]
y=nimage[:,[1]]
z=nimage[:,[2]]
x=x.tolist()
y=y.tolist()
z=z.tolist()

centers=[]
for i in range(k):
    temp=nimage[np.random.choice(nimage.shape[0], replace=False)]
    centers.append(temp)

for i in range(loop):
    cluster1, cluster2, cluster3,cluster4,cluster5,cluster6,cluster7,cluster8,cluster9,cluster10, vector = kmeans(centers,nimage)
    centers[0] = mean(cluster1)
    centers[1] = mean(cluster2)
    centers[2] = mean(cluster3)
    centers[3] = mean(cluster4)
    centers[4] = mean(cluster5)
    centers[5] = mean(cluster6)
    centers[6] = mean(cluster7)
    centers[7] = mean(cluster8)
    centers[8] = mean(cluster9)
    centers[9] = mean(cluster10)

npv = np.asarray(vector)
for i in range(npv.shape[0]):
    v = npv[i]
    if(v == 0):
        nimage[i]=centers[0]
    elif(v == 1):
        nimage[i]=centers[1]
    elif(v == 2):
        nimage[i]=centers[2]
    elif(v == 3):
        nimage[i]=centers[3]
    elif(v == 4):
        nimage[i]=centers[4]
    elif(v == 5):
        nimage[i]=centers[5]
    elif(v == 6):
        nimage[i]=centers[6]
    elif(v == 7):
        nimage[i]=centers[7]
    elif(v == 8):
        nimage[i]=centers[8]
    else:
        nimage[i]=centers[9]

qimg=np.reshape(nimage,(image.shape))
cv2.imwrite('task3_baboon_10.jpg',qimg)

'''******* K=20 ********'''
def kmeans(center,x):
    c1=[]
    c2=[]
    c3=[]
    c4=[]
    c5=[]
    c6=[]
    c7=[]
    c8=[]
    c9=[]
    c10=[]
    c11=[]
    c12=[]
    c13=[]
    c14=[]
    c15=[]
    c16=[]
    c17=[]
    c18=[]
    c19=[]
    c20=[]
    vector=[]
    for i in range(len(x)):
        temp=[]
        minimum=1000
        index=0
        for j in range(len(center)):
            l=ed(center[j],x[i])
            temp.append(l)
        for k in range(len(temp)):
            if(temp[k]<minimum):
                minimum=temp[k]
                index=k
        if(index==0):
            c1.append(x[i])
            vector.append(0)
        elif(index==1):
            c2.append(x[i])
            vector.append(1)
        elif(index==2):
            c3.append(x[i])
            vector.append(2) 
        elif(index==3):
            c4.append(x[i])
            vector.append(3)
        elif(index==4):
            c5.append(x[i])
            vector.append(4)
        elif(index==5):
            c6.append(x[i])
            vector.append(5)
        elif(index==6):
            c7.append(x[i])
            vector.append(6)
        elif(index==7):
            c8.append(x[i])
            vector.append(7)
        elif(index==8):
            c9.append(x[i])
            vector.append(8)
        elif(index==9):
            c10.append(x[i])
            vector.append(9)
        elif(index==10):
            c11.append(x[i])
            vector.append(10)
        elif(index==11):
            c12.append(x[i])
            vector.append(11)
        elif(index==12):
            c13.append(x[i])
            vector.append(12)
        elif(index==13):
            c14.append(x[i])
            vector.append(13)
        elif(index==14):
            c15.append(x[i])
            vector.append(14)
        elif(index==15):
            c16.append(x[i])
            vector.append(15)
        elif(index==16):
            c17.append(x[i])
            vector.append(16)
        elif(index==17):
            c18.append(x[i])
            vector.append(17)
        elif(index==18):
            c19.append(x[i])
            vector.append(18)
        else:
            c20.append(x[i])
            vector.append(19)
    return c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,vector

k=20
loop=18
image=cv2.imread('baboon.jpg')
nimage=np.reshape(image,(-1,3))
x=nimage[:,[0]]
y=nimage[:,[1]]
z=nimage[:,[2]]
x=x.tolist()
y=y.tolist()
z=z.tolist()

centers=[]
for i in range(k):
    temp=nimage[np.random.choice(nimage.shape[0], replace=False)]
    centers.append(temp)

for i in range(loop):
    cluster1, cluster2, cluster3,cluster4,cluster5,cluster6,cluster7,cluster8,cluster9,cluster10,cluster11, cluster12, cluster13,cluster14,cluster15,cluster16,cluster17,cluster18,cluster19,cluster20, vector = kmeans(centers,nimage)
    centers[0] = mean(cluster1)
    centers[1] = mean(cluster2)
    centers[2] = mean(cluster3)
    centers[3] = mean(cluster4)
    centers[4] = mean(cluster5)
    centers[5] = mean(cluster6)
    centers[6] = mean(cluster7)
    centers[7] = mean(cluster8)
    centers[8] = mean(cluster9)
    centers[9] = mean(cluster10)
    centers[10] = mean(cluster11)
    centers[11] = mean(cluster12)
    centers[12] = mean(cluster13)
    centers[13] = mean(cluster14)
    centers[14] = mean(cluster15)
    centers[15] = mean(cluster16)
    centers[16] = mean(cluster17)
    centers[17] = mean(cluster18)
    centers[18] = mean(cluster19)
    centers[19] = mean(cluster20)

npv = np.asarray(vector)
for i in range(npv.shape[0]):
    v = npv[i]
    if(v == 0):
        nimage[i]=centers[0]
    elif(v == 1):
        nimage[i]=centers[1]
    elif(v == 2):
        nimage[i]=centers[2]
    elif(v == 3):
        nimage[i]=centers[3]
    elif(v == 4):
        nimage[i]=centers[4]
    elif(v == 5):
        nimage[i]=centers[5]
    elif(v == 6):
        nimage[i]=centers[6]
    elif(v == 7):
        nimage[i]=centers[7]
    elif(v == 8):
        nimage[i]=centers[8]
    elif(v == 9):
        nimage[i]=centers[9]
    elif(v == 10):
        nimage[i]=centers[10]
    elif(v == 11):
        nimage[i]=centers[11]
    elif(v == 12):
        nimage[i]=centers[12]
    elif(v == 13):
        nimage[i]=centers[13]
    elif(v == 14):
        nimage[i]=centers[14]
    elif(v == 15):
        nimage[i]=centers[15]
    elif(v == 16):
        nimage[i]=centers[16]
    elif(v == 17):
        nimage[i]=centers[17]
    elif(v == 18):
        nimage[i]=centers[18]
    elif(v == 19):
        nimage[i]=centers[19]
    elif(v == 20):
        nimage[i]=centers[20]

qimg=np.reshape(nimage,(image.shape))
cv2.imwrite('task3_baboon_20.jpg',qimg)