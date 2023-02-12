#!/usr/bin/env python
# coding: utf-8

# In[41]:


#The Inputs
input_year = int(input(""))
input_day = int(input(""))

#Part I
#Possible Scenarios
scenario_1 = input_year%4==0 and not (input_year%100==0 and input_year%400==0)
scenario_2 = input_year%4==0 and input_year%100==0 and not input_year%400==0
scenario_3 = input_year%4==0 and input_year%100==0 and input_year%400==0

leap_year = bool(scenario_1) + bool(scenario_3) - bool(scenario_2)
leap_year == 1


#print(leap_year)

#Part II

#Finding The Month

jan = (input_day>=1) == 1
feb = (input_day>=32) == 1
mar = (input_day>=(60+leap_year)) == 1
apr = (input_day>=(91+leap_year)) == 1
may = (input_day>=(121+leap_year)) == 1
jun = (input_day>=(152+leap_year)) == 1
jul = (input_day>=(182+leap_year)) == 1
aug = (input_day>=(213+leap_year)) == 1
sep = (input_day>=(244+leap_year)) == 1
octb = (input_day>=(274+leap_year)) == 1
nov = (input_day>=(305+leap_year)) == 1
dec = (input_day>=(335+leap_year)) == 1


the_month = jan +feb +mar +apr +may +jun +jul +aug +sep +octb +dec

#Finding The Day

day_m1  = (the_month==1) * (input_day) - 1
day_m2  = (the_month==2) * (input_day - 31) +1
day_m3  = (the_month==3) * (input_day - (60 + leap_year) +1)
day_m4  = (the_month==4) * (input_day - (91 + leap_year) +1)
day_m5  = (the_month==5) * (input_day - (121 + leap_year) +1)
day_m6  = (the_month==6) * (input_day - (152 + leap_year) +1)
day_m7  = (the_month==7) * (input_day - (182 + leap_year) +1)
day_m8  = (the_month==8) * (input_day - (213 + leap_year) +1)
day_m9  = (the_month==9) * (input_day - (244 + leap_year) +1)
day_m10 = (the_month==10) * (input_day - (274 + leap_year) +1)
day_m11 = (the_month==11) * (input_day - (305 + leap_year) +1)
day_m12 = (the_month==12) * (input_day - (335 + leap_year) +1)

the_day = str(day_m1 + day_m2 + day_m3 + day_m4 + day_m5 + day_m6 + day_m7 + day_m8 + day_m9 + day_m10 + day_m11 + day_m12)

#Final Prints
print(leap_year*"True" + ((1-leap_year)*"False"))
print(str(the_day) + "/" + str(the_month) + "/" + str(input_year))

