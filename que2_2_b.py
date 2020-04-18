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




  
    
c=0
relevence_original=[]
relenvce_list_only_sorted=[]
relenvce_list_only=[]
for i in y:
    if i[1]=='qid:4':
        x=[]
        x.append(c)
        x.append(int(i[0]))
        relevence_original.append(x)
        relenvce_list_only.append(int(i[0]))

#sort the relenvce_list_only
relenvce_list_only1=relenvce_list_only
relenvce_list_only_sorted=sorted(relenvce_list_only1,reverse=True)

#calculate IDCG:
IDCG=0
import math
count1=0
for i in relenvce_list_only_sorted:
        IDCG=IDCG+(i/math.log((count1+2),2))
        count1=count1+1
print("IDCG:",IDCG)
    
#calculate DCG
DCG=0
#import math
count2=0
for i in relenvce_list_only1:
    DCG=DCG+(i/math.log((count2+2),2))
    count2=count2+1
print("DCG:",DCG)


print("nDCG:",DCG/IDCG)