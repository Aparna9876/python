#!/usr/bin/env python
# coding: utf-8

# # Lists
# 

# In[1]:


a=["Hello",20,67.4,[3,6,1.4]]
print(a)


# In[2]:


a


# In[3]:


a[0]


# In[4]:


a[4]


# In[5]:


a[3]


# In[6]:


a[-3]


# In[7]:


a[2:]


# In[8]:


a[:-1]


# In[9]:


a[:]


# In[10]:


a[-2:1]


# In[11]:


#By Default Methods in Lists


# In[12]:


a.copy()


# In[13]:


b=a.copy()


# In[14]:


b


# In[15]:


a.clear()


# In[16]:


a


# In[17]:


b


# In[18]:


b.count(20)


# In[19]:


b.extend(20)


# In[20]:


help(b.extend())


# In[21]:


b.append(20)


# In[22]:


b.count()


# In[23]:


b.count(20)


# In[24]:


b.index(20)


# In[25]:


b


# In[26]:


b.index(67.4)


# In[27]:


b.insert("hi")


# In[28]:


b.insert("hi",2)


# In[36]:


b


# In[30]:


b.insert(2,"hi")


# In[32]:


b.pop()


# In[34]:


b.pop(4)


# In[35]:


b.remove(20)


# In[37]:


b


# In[38]:


b.reverse()


# In[39]:


b


# In[40]:


b.index(67.4)


# In[41]:


b.sort()


# In[42]:


c=[3,6,1,7,2]
c


# In[43]:


c.sort()


# In[44]:


c


# In[45]:


help(b.extend)


# In[49]:


i=2
c.extend(i)


# In[51]:


extend(c)


# # Dictionaries

# In[52]:


a={"Name":"Aparna",
  "Reg No":"11189A227",
  "Gmail":"surabattiniaparna@gmail.com"}
a


# In[53]:


a.get("Name")


# In[54]:


a["Gmail"]


# In[55]:


a.get(Ph no)


# In[56]:


a[Reg No]


# In[57]:


a["Reg No"]


# In[58]:


b=a.copy()


# In[59]:


b


# In[60]:


a.clear()


# In[61]:


a


# In[62]:


b


# In[63]:


help(b.fromkeys)


# In[64]:


# lists
b.extend([1,2,3])


# In[65]:


#lists
c.extend([1,5,4])


# In[66]:


c


# In[70]:


b.fromkeys("Gmail")


# In[71]:


b.items()


# b.keys()

# In[72]:


b.keys()


# In[73]:


b.fromkeys('Name')


# In[74]:


b.pop()


# In[75]:


help(b.pop)


# In[76]:


b.pop("Gmail")


# In[77]:


b


# In[78]:


b.popitem()


# In[79]:


b


# In[82]:


a={"a":1,"b":2,"c":3}


# In[83]:


a


# In[84]:


b=a.setdefault("c",4)


# In[85]:


b


# In[86]:


a


# In[ ]:


a.setdefault("d",4)


# In[88]:


a


# In[89]:


a.setdefault("c",5)


# In[96]:


v=a.values()


# In[97]:


v


# In[ ]:


a.update({"e":5,"f":6})


# # Tuples

# In[98]:


x=(4,7,2,4,6,7.98,"hi")


# In[99]:


x


# In[100]:


x.count(4)


# In[101]:


x.index(7.98)


# # Sets

# In[102]:


colors={"orange","pink","blue","green","yellow"}


# In[116]:


colors


# In[110]:


colors.add(56)


# In[114]:


a


# In[115]:


colors.clear()


# In[126]:


x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=y.isdisjoint(x)
print(z)


# In[123]:


x


# In[121]:


y


# In[122]:


x.discard("apple")


# In[127]:


p={1,2,3,4,5}
q={1,2,3}
r=p.issubset(q)
print(r)


# In[128]:


p={1,2,3,4,5}
q={1,2,3}
r=p.issuperset(q)
print(r)


# In[129]:


p.pop()


# In[132]:


q.remove(3)


# In[131]:


help(q.remove)


# In[133]:


q


# In[135]:


q.add(7)


# In[136]:


p={1,2,3,4,5}
q={1,2,3}
r=p.union(q)
print(r)


# In[139]:


p={1,2,3,4,5}
q={1,2,8}
r=p.symmetric_difference_update(q)
print(r)


# In[138]:


p={1,2,3,4,5}
q={1,2,7,8}
r=p.union(q)
print(r)


# In[140]:


p={1,2,3,4,5}
q={1,2,3}
p.update(q)
print(p)
print(q)


# In[141]:


a="Aparna"


# In[142]:


a.capitalize()


# In[143]:


a


# In[144]:


a.casefold()


# In[145]:


a.center()


# In[146]:


a.center(20)


# In[147]:


a.count("a")


# In[148]:


z=a.endswith("na")


# In[149]:


z


# In[150]:


c=a.encode()
c


# In[151]:


s=a.find('arn')


# In[152]:


s


# In[153]:


a.index('r')


# In[154]:


a.isalpha()


# In[155]:


a.isalnum()


# In[156]:


a.isdecimal()


# In[157]:


a.casefold()


# In[158]:


a.islower()


# In[159]:


a.isprintable()


# In[160]:


t="APARNA"


# In[161]:


t.istitle()


# In[162]:


a.swapcase()


# In[166]:


a.zfill("a")


# In[167]:


len(a)


# In[168]:


t.startswith("A")


# In[ ]:




