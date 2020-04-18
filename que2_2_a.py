# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 02:39:15 2020

@author: akanksha
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 22:44:52 2020

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


#final answer in pikle file
import pandas as pd
df = pd.DataFrame()
for i in range(0,len(y)):
    xc=[]
    xc=y[i]
    if xc[1]=='qid:4':
        df[i]=y[i]
df=df.T
dfObj = df.sort_values(by =0 ,ascending=False)
import pickle
pickle_out = open("que2_a.pkl","wb")
pickle.dump(dfObj, pickle_out)
pickle_out.close()
    
c=0
relevence_original=[]
relenvce_list_only_sorted=[]
relenvce_list_only=[]


def perm(a):
    n=0
    for i in range(0,a+1):
        n=n+(math.factorial(a)/math.factorial(a-i))
    print("n:",n)
    return n

def permuatation():
    c3=0
    c2=0
    c1=0
    c0=0
    for i in relenvce_list_only111:
        if i==3:
            c3=c3+1
        if i==2:
            c2=c2+1
        if i==1:
            c1=c1+1
        if i==0:
            
            c0=c0+1
    print(c3)
    print(c2)
    print(c1)
    print(c0)
    permut=math.factorial(c3)*math.factorial(c2)*math.factorial(c1)*perm(c0)
    print(permut)
    

permuatation()

for i in y:
    if c<50:
       
        if i[1]=='qid:4':
            x=[]
            x.append(c)
            x.append(int(i[0]))
            relevence_original.append(x)
            relenvce_list_only.append(int(i[0]))
    c=c+1

#sort the relenvce_list_only
relenvce_list_only1=relenvce_list_only
relenvce_list_only_sorted=sorted(relenvce_list_only1,reverse=True)


#sort b4 pick up:
c11=0
relevence_original11=[]
relenvce_list_only_sorted11=[]
relenvce_list_only11=[]
for i in y:
    if i[1]=='qid:4':
        x=[]
        x.append(c11)
        x.append(int(i[0]))
        relevence_original.append(x)
        relenvce_list_only11.append(int(i[0]))

#sort the relenvce_list_only
relenvce_list_only111=relenvce_list_only11
relenvce_list_only_sorted11=sorted(relenvce_list_only11,reverse=True)
#calculate IDCG:

import math
IDCG=0
count1=0
for i1 in relenvce_list_only_sorted11:
    if count1<50:       
        IDCG=IDCG+(i1/math.log((count1+2),2))
    count1=count1+1
print("IDCG:",IDCG)
    
#calculate DCG
DCG=0
#import math
count2=0
for i in relenvce_list_only:
    if count2<50:
        
        DCG=DCG+(i/math.log((count2+2),2))
        count2=count2+1
print("DCG:",DCG)


print("nDCG:",DCG/IDCG)

