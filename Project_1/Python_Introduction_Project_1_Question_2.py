#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Some_Variables
char_1 = input("")
char_2 = input("")
char_3 = input("")
num_1 = int(input(""))
num_2 = int(input(""))

#last len
part_2_len = (num_2-num_1)
is_part_2_positive = part_2_len>=0
new_real_len = is_part_2_positive*part_2_len

#Printing_Time
print(char_1*num_1 + char_3*new_real_len + (char_2+char_3)*(int(num_2/num_1)*2) )
print(num_1+ int(num_2/num_1)*4 + new_real_len)


# In[ ]:





# In[ ]:




