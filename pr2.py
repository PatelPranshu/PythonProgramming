#!/usr/bin/env python
# coding: utf-8

# In[16]:


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(my_list)


# In[17]:


l[11]="cspit"

print(my_list)


# In[18]:


print(l[2:15:4])
print(l[14:1:-4])
print(l[-6:-19:-4])
l.append(200)
print(l)


# In[19]:


l1=l+[300,400]
print(l)


# In[20]:


l.insert(5,'charusat')
print(l)


# In[21]:


l.remove('cspit')
print(l)


# In[23]:


l.pop()
del l[5]
print(l)


# In[27]:


a,b,*c=l
print(a,b,c)


# In[29]:


a,b,*c,d,e=l
print(a,b,c,d,e)


# In[31]:


print(4 in l)
print(300 in l)
print(l.index(4))


# In[33]:


print(l.count(15))


# In[34]:


l.reverse()
print(l)


# In[38]:


l.sort(reverse=True)
print(l)


# In[39]:


print(sorted(l))


# In[ ]:





# In[47]:


List1 = [1, 2, 3, 4, ["python", "java", "c++", [10, 20, 30]], 5, 6, 7, ["apple", "banana", "orange"]]

print(List1[-1][-1])
print(List1[4][0])

# RepeatedList = List1[::1]
RepeatedList = [List1] * 5
print(RepeatedList)




# In[ ]:





# In[ ]:




