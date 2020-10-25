# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 00:31:58 2020

@author: BICHA
"""

from covid import Covid
import matplotlib.pyplot as pt

covid = Covid()

name = input("Enter the Country Name ")

vdata = covid.get_status_by_country_name(name)
remove = ['id','country','latitude','longitude','last_update']
for i in remove:
    vdata.pop(i)
all = vdata.pop('confirmed')
print(vdata)

id = list(vdata.keys())
value = [str(i) for i in vdata.values()]

pt.pie(value, labels = id , colors = ['r','g','b'], autopct = '%1.1f%%')
pt.title("COUNTRY: " +name.upper() +"\n TOTAL CASES : "+str(all))
pt.legend()
pt.show()