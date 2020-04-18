# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 03:05:40 2020

@author: akanksha
"""

import os
ff = open("C:/Users/akanksha/Desktop/IR-assignment-3-data.txt", "r+",encoding="utf-8",errors='ignore')
tt=ff.read()
gd={}
t=[]
y=[]
t=tt.split("\n")
for i in t:
    y.append(i.split(" "))

#remove '' from the list  
for i in y:
    i.remove('')
  
y.remove([])  




  
#taking only 75 column    
c=0
relevence_original=[]
qid_75=[]

for i in y:
    #print(i[76].startswith('75:'))
    if i[76].startswith('75:')==True and i[1]=='qid:4':
        x=[]
        x.append(i[76].split(":"))
        relevence_original.append(i[0])
        #z=[]
        #z.append(i[1])
        qid_75.append(float(x[0][1]))
        #z.append(float(x[0][1]))
        #qid.append(z)
        c=c+1




qid_75_new=qid_75
qid_75_sorted=sorted(qid_75,reverse=True)

df=relevence_original
relevence_sorted=sorted(df,reverse=True)

g=0
for i in relevence_sorted:
   if i=='0':
       break
   else:
       g=g+1

#sort on the basis col 75
X = relevence_original
Y = qid_75_sorted

Z = [x for _,x in sorted(zip(Y,X),reverse=True)]
Z=list(map(int, Z))
print(Z) 
print(Y)


x_axis=[]     
Precision=[]
Recall=[]  
Precision.append(1)
Recall.append(0)
def ret():
    count=0
    for i in range(0,len(Z)):
        if Z[i]>0:
           count=count+1 
        p=count/(i+1)      
        r=count/g
        print("count:",count)
        Precision.append(p)
        Recall.append(r)
        x_axis.append(i+1)
        




import matplotlib.pyplot as plt 
def main():
    ret()
    print("Precision-",Precision)
    print("Recall-",Recall)
    plt.plot( Recall,Precision, label = "precision") 
   # plt.plot(, x_axis, label = "recall") 
    plt.xlabel('Recall') 
    # naming the y axis 
    plt.ylabel('Precision') 
# giving a title to my graph 
    #plt.title('Two lines on same graph!') 
   

# function to show the plot 
    plt.show() 
main()