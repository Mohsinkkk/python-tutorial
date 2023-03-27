#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Hello world")


# In[4]:


student="sam"


# In[5]:


student


# In[6]:


student="john"


# In[7]:


student


# In[8]:


student="matt"


# In[9]:


student


# In[10]:


#Arithmetic operators
# +,-,/,*


# In[12]:


a = 10
b = 20


# In[13]:


a,b


# In[14]:


a+b


# In[15]:


a-b


# In[16]:


a/b


# In[17]:


a*b


# In[18]:


#Relational operators
# <,>,==,!=


# In[19]:


a = 50
b = 100


# In[20]:


a>b


# In[21]:


a<b


# In[22]:


a==b


# In[23]:


a!=b


# In[24]:


#Logical operators
# &,|


# In[26]:


a = True
b = False


# In[27]:


a & a


# In[28]:


a & b


# In[29]:


b & a


# In[30]:


b & b


# In[31]:


a | a


# In[32]:


a | b


# In[33]:


b | a


# In[34]:


b | b


# In[35]:


str1 = 'this is my First string'


# In[36]:


str1


# In[37]:


str2 = "this is my second string"


# In[38]:


str2


# In[44]:


str3 = '''

This string 
has
lot of lines
ikn it
'''


# In[45]:


str3


# In[46]:


my_string = 'This is sparta'


# In[47]:


my_string


# In[49]:


my_string[0]


# In[51]:


my_string[-1]


# In[54]:


my_string[5:11]


# In[57]:


my_string = 'this is sparta'


# In[59]:


my_string


# In[61]:


len(my_string)


# In[64]:


my_string.lower()


# In[66]:


my_string.upper()


# In[67]:


my_string.replace('is','are')


# In[69]:


str_new = 'sparta sparta 300 300 300 300 s'
str_new


# In[71]:


str_new.count('sparta')


# In[72]:


str_new.count('300')


# In[74]:


my_string = 'hello world is awesome'
my_string.find('i')


# In[75]:


str_final = 'president obana is the best president of united states'


# In[77]:


str_final


# In[79]:


str_final.split('e')


# In[4]:


# Data Strucute in python(tuple)
tup1 = (1,True,3.14,5-7j)
tup1


# In[5]:


type(tup1)


# In[6]:


tup1 = (1,"a",True,2,"b",False)
tup1[0]


# In[8]:


tup1 = (1,"a",True,2,"b",False)
tup1[-1]


# In[12]:


tup1 = (1,"a",True,2,"b",False)
tup1[1:4]


# In[13]:


#Finding Lengths of tuples
tup1 = (1,"a",True,2,"b",False)
len(tup1)


# In[14]:


# Concatenating Tuples
tup1 = (1,2,3)
tup2 = (4,5,6)
tup1+tup2


# In[15]:


#repeating tuple elements
tup1 = ('sparta',300)
tup1*3


# In[16]:


#repeating and concatenating
tup1 = ('sparta',300)
tup2 = (4,5,6)
tup1*3 + tup2


# In[17]:


#minimum value
tup1 = (1,2,3,4,5)
min(tup1)


# In[18]:


#maximum value
tup1 = (1,2,3,4,5)
max(tup1)


# In[2]:


#Data structure in python 2.(List)
l1 = [1,'sparta',3.14,True]
l1


# In[3]:


type(l1)


# In[5]:


l1[0]


# In[6]:


l1[-1]


# In[7]:


l1[1:3]


# In[9]:


#modifying a List
#changing the element at 0th index
l1=[1,"a",2,"b",3,"c"]
l1[0]=100
l1


# In[10]:


#Appending a new elemnts
l1 =[1,"a",2,"b",3,"c"]
l1.append("Sparta")
l1


# In[12]:


#poping the last elements
l1 =[1,"a",2,"b",3,"c"]
l1.pop()
l1


# In[13]:


#reverse elemnts of alist
l1 =[1,"a",2,"b",3,"c"]
l1.reverse()
l1


# In[14]:


#inserting elements at a specified index
l1 =[1,"a",2,"b",3,"c"]
l1.insert(1,"sparta")
l1


# In[15]:


#sorting a list
l1 =["mango","banana","guava","apple"]
l1.sort()
l1


# In[16]:


#List Basic Operations
#Concatenating list
l1 =[1,2,3]
l2 =["a","b","c"]
l1+l2


# In[17]:


#repeating elements
l1 =[1,"a",True]
l1*3


# In[18]:


#Data structure in python 3.(Dictionary)
d1 ={"Apple":50,"mango":100,"Guava":200,"Banana":500}
d1


# In[19]:


type(d1)


# In[20]:


#Extracting keys
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40}
fruit.keys()


# In[21]:


#Extracting values
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40}
fruit.values()


# In[25]:


#Adding a new elements
fruit={"Apple":10,"Oranges":20,"Banana":30,"Guava":40}
fruit["Mango"]=50
fruit


# In[27]:


#Changing an existing element
fruit={"Apple":10,"Oranges":20,"Banan":30,"Guava":40,"Mango":50}
fruit["Apple"]=100
fruit


# In[31]:


#update one dictionary's elements with another
fruit1={"Apple":10,"Oranges":20,}
fruit2={"Banana":30,"Guava":40}
fruit1.update(fruit2)
fruit1


# In[1]:


#pop one dictionay's elements
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40}
fruit.pop("Orange")
fruit


# In[2]:


#Data structure in python 4.(set)
#Update one dictionary's elements with another
s1={1,"a",True,2,"b",False}
s1.add("Hello")
s1


# In[3]:


#Update multiple elements
s1={1,"a",True,2,"b",False}
s1.update([10,20,30])
s1


# In[4]:


#Remove an element
s1={1,"a",True,2,"b",False}
s1.remove("b")
s1


# In[5]:


#set Function
#union of two set
s1={1,2,3}
s2={4,5,6}
s1.union(s2)


# In[6]:


#intersection of two sets
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
s1.intersection(s2)


# In[7]:


#decision making statements
a=10
b=20
if a>b:
    print("A is greater than B")
else:
    print("B is greater than A")


# In[9]:


a=10
b=20
c=30
if (a>b) & (a>c):
    print("A is the greatest")
elif (b>a) & (b>c):
    print("B is the greatest")
else:
    print("C is the greatest")


# In[2]:


a=10
b=50
c=30
if (a>b) & (a>c):
   print("A is greatest")
elif (b>a) & (b>c):
   print("B is greatest")
else:
   print("c is greatest")


# In[3]:


#if with tuple
tup1 = ('a','b','c')
if 'a' in tup1:
    print("Value a is present in tup1")
else:
    print("Value a is not present in tup1")


# In[10]:


#if with list
l1 = ['a','b','c']
if l1[1]=='b':
    l1[1]='z'
l1    


# In[14]:


#if wih dictionary
d1 = {'k1':10,'k2':20,'k3':30}
if d1['k3'] == 30:
    d1['k3']=d1['k3']+100
d1        


# In[ ]:


#Looping statemnts
#While Lopps
i=1
while i<=10:
    print(i)
    i=i+1


# In[ ]:




