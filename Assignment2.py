#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("Please type marks of subjects below:")
English = int(input("Enter marks of English"))
Urdu = int(input("Enter marks of Urdu!"))
Maths = int(input("Enter Marks of maths:"))
Total = int(English) + int(Urdu) + int(Maths)
print("=====================================")
print("Marks Gained: "+ str(Total))
print("=====================================")
persubjmarks = 100
totalmarks = int(persubjmarks) * int(3)
print("Total Marks :"+ str(totalmarks))
totalperc = int(Total) / int(300) * int(100)
print ("Total Percantage is :"+str(totalperc)+ "%" )
if totalperc >= 80 and totalperc <= 100:
    print("A+")
elif totalperc >=70 and totalperc < 60:
    print("A")
elif totalperc >=60 and totalperc < 70:
    print("B")
elif totalperc >=0 and totalperc < 60:
    print("Fail")
else:
    print("You enterd wrong marks")


# In[2]:


num = int(input("Enter Number"))
if num %2==0:
    print("Number is Even")
else:
    print("Number is odd")
    


# In[1]:


print("LENGTH OF THE LIST")
a = [1,2,5,3,1,6,]
print(len(a))


# In[2]:


a = [1,2,5,3,1,6,]
print (sum(a))


# In[4]:


list1 = [10, 20, 4, 45, 9] 
print("Largest element is:", max(list1)) 


# In[32]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
newList = [item for item in a if item < 5]
print(newList)


# In[ ]:




