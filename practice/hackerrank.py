#!/bin/python

import sys


arr = [[1,1,1,0,0,0],
       [0,1,0,0,0,0],
       [1,1,1,0,0,0],
       [0,0,2,4,4,0],
       [0,0,0,2,0,0],
       [0,0,1,2,4,0]]

#print arr[3][3]

hour = [[1,1,1],
        [0,1,0],
        [1,1,1]]

#print hour[2][2]

a=0
b=0
x=0
res = []
temp = []
sum = []
for k in range(0,16,1):
    l=0
    m=0
    for i in range(a,a+3,1):
        l=0
        for j in range(b,b+3,1):
            gos=hour[m][l]*arr[i][j]
            temp.append(gos)
            #print temp
            l=l+1
        res.append(temp)
        temp=[]
        m=m+1
        
    print res
    for num in res:
        for n in num:
            x = x + n
    sum.append(x)
    x=0
    print sum
    res=[]
    b=b+1
    if b>3:
        b=0
        a=a+1

print(max(sum))

    
