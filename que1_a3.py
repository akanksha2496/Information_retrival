# -*- coding: utf-8 -*-
"""que1_A3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ChOHZu128-TX-NGR3oieH1v3B2hagve_
"""



import numpy as np 
import os 
###https://www.geeksforgeeks.org/working-zip-files-python/
##import zip code from here

# importing required modules 
from zipfile import ZipFile 


  
# opening the zip file in READ mode 
with ZipFile('/content/20_newsgroups.zip', 'r') as zip: 
    # printing all the contents of the zip file 
    # zip.printdir() 
  
    # extracting all the files 
    print('Extracting all the files now...') 
    zip.extractall()
    print('Done!')

#reading
import glob
foldername=glob.glob("/content/20_newsgroups/*")

pip install num2words

from nltk.stem import WordNetLemmatizer 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from num2words import num2words 
import re
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def preprocessing(data):
  f_l=[]
  s = "" 
  lines = [data.lower()]
  punct= [re.sub('[^A-Za-z0-9]+', ' ', word) for word in lines]   
 
  for e in punct:  
    s=s+ e         
  stop_words = set(stopwords.words('english'))
  tokens = word_tokenize(s)
  r = [i for i in tokens if not i in stop_words]
  lemmatizer = WordNetLemmatizer() 
  lem = [lemmatizer.lemmatize(x) for x in r]
  for i in lem:
    
    if i.isnumeric()==False:
      f_l.append(i)
    
    if i.isnumeric()==True:
      n=num2words(i)
      
      n=n.replace('-',' ')
      
      n=n.replace(' and','')
      
      n=n.replace(',','')
    
      n=n.split()
    
      for n1 in n:
        f_l.append(n1)
  f_list=[]
  return f_l

unique_words=[]
document_id=[]
document_path={}
inverted_index={}
count=0
for files in foldername:
    #read files
    file=glob.glob(files+"/*")
    # print(type(file))
    for i in file:
    #list ko read karaa hai yha pe because text files pura list ke form hai\n",
        count=count+1
        document_id.append(count) 
        f=open(i,'r',encoding='utf-8',errors="ignore")       
        document_path[count]=i
        text=f.read()
        final_tokens=preprocessing(text)
        # print("final:",final_tokens)
        for j in final_tokens:
            if count in inverted_index.keys():
                inverted_index[count].append(j)
                if j not in unique_words:
                  unique_words.append(j)
            else:
                inverted_index[count]=[]
                inverted_index[count].append(j)
                if j not in unique_words:
                  unique_words.append(j)
            
        document_path[count]=i





# key_list = list(document_path.keys()) 
# val_list = list(document_path.values()) 
  
# print(key_list[val_list.index('/content/20_newsgroups/alt.atheism/49960')]) 
# # print(key_list[val_list.index(112)])

ff = open("file.txt", "r+",encoding="utf-8",errors='ignore')
tt=ff.read()
gd={}
t=tt.split("\n")
for i in t:
  t1=i.split(" ")
  # print("t1",t1)
  gd[int(t1[0])]=int(t1[1])

import numpy as np

def NormalizeData(data):
    all_values = gd.values()
    max_key = max(all_values)
    min_key = min(all_values)
    
    return (data -min_key) / (max_key - min_key)

gd_norm=gd

for i in gd.keys():
  gd_norm[i]=NormalizeData(gd[i])

# gd is score of documents
# inverted_index is index of document_id:terms
# document_path= path of dumnet documt id wise

term_dictionary={}

import numpy as np

for i in range(1,len(inverted_index)+1):
  for j in unique_words:
    if j in inverted_index[i]:
      if j in term_dictionary.keys():
        term_dictionary[j].append((i,inverted_index[i].count(j)))
      else:
        term_dictionary[j]=[]
        term_dictionary[j].append((i,1+np.log(inverted_index[i].count(j)+1)))

"""pickle file of tf:"""

import pickle 
pickle_in = open("/content/drive/My Drive/myfile.pkl","rb")
Tf_dictionary = pickle.load(pickle_in)

Tf_dictionary_new=Tf_dictionary

# import operator
# for i in Tf_dictionary.keys():
#   Tf_dictionary_new[i]=Orde(orted(Tf_dictionary_new[i].items(), key=operator.itemgetter(1),reverse=True)

"""gd appendedd:"""

for i in Tf_dictionary.keys():
  for j in Tf_dictionary[i].keys():
    Tf_dictionary[i][j]=[Tf_dictionary[i][j],gd[j]]

gd

Tf_dictionary

"""sorted on the basis of tf:"""

from collections import OrderedDict
for i in Tf_dictionary.keys():
  
  Tf_dictionary[i] = OrderedDict(sorted(Tf_dictionary[i].items(), key=lambda x: x[1],reverse=True))

Tf_dictionary['xref'].keys()

"""heuristic for choosing r :"""

s=0
for i in Tf_dictionary.keys():
  s=s+len(Tf_dictionary[i])
r_value=s/len(Tf_dictionary.keys())
print(s/len(Tf_dictionary.keys()))

"""split on the baisis of r high list or low list:"""

Tf_dictionary_high={}
Tf_dictionary_low={}
for i in Tf_dictionary.keys():
  r=20
  if(r>len(Tf_dictionary[i])):
    Tf_dictionary_high[i]=[]
    Tf_dictionary_low[i]=[]
    c=0
    for j in Tf_dictionary[i].keys():
      if(c==r):
        break
      Tf_dictionary_high[i].append((j,Tf_dictionary[i][j]))
      c=c+1
  else:
    Tf_dictionary_high[i]=[]
    Tf_dictionary_low[i]=[]
    c=0
    new_l=[]
    for x in Tf_dictionary[i].keys():
      new_l.append(x)
    for j in Tf_dictionary[i].keys():
      if(c==r):
        break
      Tf_dictionary_high[i].append((j,Tf_dictionary[i][j]))
      c=c+1
    for j in range(c,len(Tf_dictionary[i])):
      Tf_dictionary_low[i].append((new_l[j],Tf_dictionary[i][new_l[j]]))
  Tf_dictionary_high[i]=OrderedDict(Tf_dictionary_high[i])
  Tf_dictionary_low[i]=OrderedDict(Tf_dictionary_low[i])



"""sort in gd order"""

len(Tf_dictionary_high['xref'])



"""swap elemnts of high and low list: and sort on the  basis of gd"""

for i in Tf_dictionary_high.keys():
  for j in Tf_dictionary_high[i].keys():
    temp=Tf_dictionary_high[i][j][0]
    Tf_dictionary_high[i][j][0]=Tf_dictionary_high[i][j][1]
    Tf_dictionary_high[i][j][1]=temp

for i in Tf_dictionary_low.keys():
  for j in Tf_dictionary_low[i].keys():
    temp=Tf_dictionary_low[i][j][0]
    Tf_dictionary_low[i][j][0]=Tf_dictionary_low[i][j][1]
    Tf_dictionary_low[i][j][1]=temp

for i in Tf_dictionary_high.keys():
  
  Tf_dictionary_high[i] = OrderedDict(sorted(Tf_dictionary_high[i].items(), key=lambda x: x[1],reverse=True))

for i in Tf_dictionary_low.keys():
  
  Tf_dictionary_low[i] = OrderedDict(sorted(Tf_dictionary_low[i].items(), key=lambda x: x[1],reverse=True))

for i in Tf_dictionary_low.keys():
  for j in Tf_dictionary_low[i].keys():
    temp=Tf_dictionary_low[i][j][0]
    Tf_dictionary_low[i][j][0]=Tf_dictionary_low[i][j][1]
    Tf_dictionary_low[i][j][1]=temp

for i in Tf_dictionary_high.keys():
  for j in Tf_dictionary_high[i].keys():
    temp=Tf_dictionary_high[i][j][0]
    Tf_dictionary_high[i][j][0]=Tf_dictionary_high[i][j][1]
    Tf_dictionary_high[i][j][1]=temp

# for i in Tf_dictionary_low.keys():
#   if len(Tf_dictionary_low[i])>20:
#     print(len(Tf_dictionary_low[i]))

"""list of documents in high list:"""

high_list_docs=[]
for i in Tf_dictionary_high.keys():
  for j in Tf_dictionary_high[i].keys():
    if j not in high_list_docs:
      high_list_docs.append(j)

"""list of documents in low list:"""

low_list_docs=[]
for i in Tf_dictionary_low.keys():
  for j in Tf_dictionary_low[i].keys():
    if j not in low_list_docs:
      low_list_docs.append(j)

"""calculate idf:"""

idf_dictionary={}
for i in Tf_dictionary.keys():
    idf_dictionary[i]=19997/len(Tf_dictionary[i])

idf_dictionary

"""cosine_calculation:"""

def cosine_calculate(f,query_tf,query_dict):
   cosine_cal={}
   for i in f:
     print("doc id : ",i)
     s1=0
     s2=0
     s3=0
     for j in query_dict.keys():
       c=list(Tf_dictionary_high[j].keys())
       if i in c:  
         s1=s1+(Tf_dictionary_high[j][i][0]*idf_dictionary[j])*(query_tf[j]*idf_dictionary[j])
         s2=s2+(Tf_dictionary_high[j][i][0]*idf_dictionary[j])**2
         s3=s3+(query_tf[j]*idf_dictionary[j])**2
       else:
         s1=s1+((1+math.log(1))*(19997/1))*(query_tf[j]*(19997/1))
         s2=s2+((1+math.log(1))*(19997/1))**2
         s3=s3+(query_tf[j]*(19997/1))**2
     print("s1:",s1)
     print("s2:",s2)
     print("s3:",s3)
     m=gd[i]+(s1/(math.sqrt(s2)*math.sqrt(s3)))
     print("m:",m)
     print("+++++++++++++++++++++++++++++++++")
     cosine_cal[i]=m 
   return cosine_cal



def cosine_calculate_low(f,query_tf,query_dict):
   cosine_cal={}
   for i in f:
     print("doc id : ",i)
     s1=0
     s2=0
     s3=0
     for j in query_dict.keys():
       c=list(Tf_dictionary_low[j].keys())
       if i in c:  
         s1=s1+(Tf_dictionary_low[j][i][0]*idf_dictionary[j])*(query_tf[j]*idf_dictionary[j])
         s2=s2+(Tf_dictionary_low[j][i][0]*idf_dictionary[j])**2
         s3=s3+(query_tf[j]*idf_dictionary[j])**2
       else:
         s1=s1+((1+math.log(1))*(19997/1))*(query_tf[j]*(19997/1))
         s2=s2+((1+math.log(1))*(19997/1))**2
         s3=s3+(query_tf[j]*(19997/1))**2
     print("s1:",s1)
     print("s2:",s2)
     print("s3:",s3)
     m=gd[i]+(s1/(math.sqrt(s2)*math.sqrt(s3)))
     print("m:",m)
     print("+++++++++++++++++++++++++++++++++")
     cosine_cal[i]=m 
   return cosine_cal

"""generate a query:"""

from nltk.tokenize import word_tokenize
 import math
 def query():
   x=input("enter the query:\n")
   token_query=preprocessing(x)
   process_query=list(set(preprocessing(x)))
   query_tf={}
   for i in process_query:
     query_tf[i]=1+math.log(token_query.count(i)+1)
   list_doc=[]
   for i in process_query:
     list_doc.append(list(Tf_dictionary_high[i].keys()))
   query_dict={}
   for i in range(0,len(process_query)):
     query_dict[process_query[i]]=list_doc[i]
  
   f=[]
   for i in query_dict.keys():
     print("i:",query_dict[i])
     f=f+query_dict[i]
   f=list(set(f))
   print("union of all documnets :",sorted(f))
   print("query tf:",query_tf)
 
   print("query dict:",query_dict)
   terms_return=cosine_calculate(f,query_tf,query_dict)
   terms_return_sorted={k: v for k, v in sorted(terms_return.items(), key=lambda item: item[1],reverse=True)}
   print("sort term dict acc val:",terms_return_sorted)

   K=int(input("enter the required document:\n"))
  #  print("term return type:",type(len(terms_return)))
   if K==len(terms_return):
    print(terms_return)

   elif K<len(terms_return):
     l=0
     terms_return_new={}
     for i in terms_return_sorted.keys():
       if l==K:
         break
       terms_return_new[i]=terms_return_sorted[i]
       l=l+1
     print(terms_return_new)
   else:
     print("???????????????????????")
     #k>len term
     list_doc=[]
     for i in process_query:
       list_doc.append(list(Tf_dictionary_low[i].keys()))
     query_dict={}
     for i in range(0,len(process_query)):
       query_dict[process_query[i]]=list_doc[i]
  
     f=[]
     for i in query_dict.keys():
       print("i:",query_dict[i])
       f=f+query_dict[i]
     f=list(set(f))
     print("union of all documnets :",sorted(f))
     print("query tf:",query_tf)
 
     print("query dict:",query_dict)
     terms_more_low_list=cosine_calculate_low(f,query_tf,query_dict)
     terms_return_low_sorted={}
     terms_return_low_sorted={k: v for k, v in sorted(terms_more_low_list.items(), key=lambda item: item[1],reverse=True)}
     l=0
     remain=K-len(terms_return)+1
     for i in terms_return_low_sorted.keys():
       if l==remain:
         break
       if i not in list(terms_return.keys()):
         terms_return.update({i:terms_return_low_sorted[i]})
       l=l+1
     print(terms_return)

# from nltk.tokenize import word_tokenize
# import math
# def query():
#   x=input("enter the query:\n")
#   token_query=preprocessing(x)
#   process_query=list(set(preprocessing(x)))
#   print("x:",x)
#   print("process_query:",process_query)
#   query_tf={}
#   for i in process_query:
#     query_tf[i]=1+math.log(x.count(i)+1)
#   print("query_tf: ",query_tf)

query()





xref

