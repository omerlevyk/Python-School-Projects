#!/usr/bin/env python
# coding: utf-8

# In[2]:


#variables
min=-10
max=40
num_1=float(input(""))
num_2=float(input(""))
num_3=float(input(""))

#range_checking
check_min_1= min>num_1
check_min_2= min>num_2
check_min_3= min>num_3

check_max_1= max<num_1
check_max_2= max<num_2
check_max_3= max<num_3

#conditionals
n_num_1 = check_min_1*min + check_max_1*max + (check_max_1+check_min_1==0)*num_1
n_num_2 = check_min_2*min + check_max_2*max + (check_max_2+check_min_2==0)*num_2
n_num_3 = check_min_3*min + check_max_3*max + (check_max_3+check_min_3==0)*num_3

in_range = (check_max_1+check_min_1) + (check_max_2+check_min_2) + (check_max_3+check_min_3)==0

print("NO ERROR"*in_range+"ERROR"*(1-in_range))

#averages
avg=(n_num_1 + n_num_2 + n_num_3)/3.0

print(f"Avg: {avg:.2f}")
print(f"Rounded Avg: {avg:.0f}")




# In[ ]:




