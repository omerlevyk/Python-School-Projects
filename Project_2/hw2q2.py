#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Part I - alphabet convert to numbers
char_1 = ord(input(""))
char_2 = ord(input(""))
char_3 = ord(input(""))

if char_1 <= 91:
    num_1 = char_1 - 64
else:
    num_1 = char_1 - 96

if char_2 <= 91:
    num_2 = char_2 - 64
else:
    num_2 = char_2 - 96

if char_3 <= 91:
    num_3 = char_3 - 64
else:
    num_3 = char_3 - 96

#part II - orgenize numbers in order
if num_1>=num_2 and num_1>=num_3:
    if num_2>=num_3:
        print(str(num_3)+str(num_2)+str(num_1))
    else:
        print(str(num_3)+str(num_1)+str(num_2))
        
if num_2>=num_1 and num_2>=num_3:
    if num_1>=num_3:
        print(str(num_3)+str(num_1)+str(num_2))
    else:
        print(str(num_1)+str(num_3)+str(num_2))
        
if num_3>=num_2 and num_3>=num_1:
    if num_1>=num_2:
        print(str(num_2)+str(num_1)+str(num_3))
    else:
        print(str(num_1)+str(num_2)+str(num_3))    


# In[ ]:




