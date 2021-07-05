import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re

import requests

from bs4 import BeautifulSoup
import re
import csv
from collections import OrderedDict
import statistics


def Reverse(lst):
    lst.reverse()
    return lst

def getNum(ee, ind):
    count = 0
    prev = ee[1][ind] > ee[1][-1]
    for i in range(1, len(ee)):
        curr = ee[i][ind] > ee[i][-1]
        if curr != prev:
            count += 1
            prev = curr
    return count

def getType(ee, count, ind):
    if count == 0:
        if ee[1][ind] > ee[1][-1]:
            return 2
        else:
            return 1
    elif count == 1:
        if ee[1][ind] > ee[1][-1]:
            return 3
        else:
            return 4
    return 5

# R111 = "http://mnregaweb4.nic.in/netnrega/app_issue.aspx?lflag=eng&source=national&labels=labels&Digest=GVEtvTyMaktJ6zoZj/EYWg&fin_year="
# R112 = "http://mnregaweb4.nic.in/netnrega/state_html/stregnojoball.aspx?lflag=eng&source=national&labels=labels&Digest=GVEtvTyMaktJ6zoZj/EYWg&fin_year="
# R31 = "http://mnregaweb4.nic.in/netnrega/demand_emp_demand.aspx?lflag=eng&file1=dmd&source=national&Digest=lU/DJg5NeLf5v8FDQ9nOhw&fin="
# R712 = "http://mnregaweb4.nic.in/netnrega/state_html/outlayvscomest.aspx?lflag=eng&source=national&labels=labels&Digest=GVEtvTyMaktJ6zoZj/EYWg&fin_year="
# R1 = "http://mnregaweb4.nic.in/netnrega/citizen_html/demregister.aspx?lflag=eng&fin_year="
# R2 = "&source=national&labels=labels&Digest=BPj0SPgjfNLE7gV08qxThw"
# R1 = "http://mnregaweb4.nic.in/netnrega/app_issue.aspx?lflag=eng&fin_year="
# R2 = "&source=national&labels=labels&Digest=NTLq4rB08dylIPaHM+1hWQ"
# R1 = "http://mnregaweb4.nic.in/netnrega/Citizen_html/financialstatement.aspx?lflag=eng&fin_year="
# R2 = "&source=national&labels=labels&Digest=cT/J7ChEq5LOfEr0AmsuAQ"
# R3 = "http://mnregaweb4.nic.in/netnrega/master_cat_status_n.aspx?lflag=eng&fin_year="
# R4 = "&source=national&labels=labels&Digest=NTLq4rB08dylIPaHM+1hWQ"

# 1.1.2
R1 = "http://mnregaweb4.nic.in/netnrega/state_html/stregnojoball.aspx?lflag=eng&fin_year="
R2 = "&source=national&labels=labels&Digest=NTLq4rB08dylIPaHM+1hWQ"
# 1.1.1
R3 = "http://mnregaweb4.nic.in/netnrega/app_issue.aspx?lflag=eng&fin_year="
R4 = "&source=national&labels=labels&Digest=NTLq4rB08dylIPaHM+1hWQ"

# (nemo)
col1 = 1
# (deno) 
col2 = 1
# R1,R2 For 7.1.1 (deno+nemo)
base_url1 = R1
base_url2 = R2 
# R3,R4 FOR 6.1.2 
base_url3 = R3 
base_url4 = R4 

years = ["2013-2014","2014-2015","2015-2016","2016-2017","2017-2018","2018-2019","2019-2020","2020-2021"]
exclude_years = ["2013-2014","2014-2015","2015-2016","2016-2017"]

states = ["ANDHRA PRADESH",
"ARUNACHAL PRADESH",
"ASSAM",
"BIHAR",
"CHHATTISGARH",
"GOA",
"GUJARAT",
"HARYANA",
"HIMACHAL PRADESH",
"JAMMU AND KASHMIR",
"JHARKHAND",
"KARNATAKA",
"KERALA",
# "LADAKH",
"MADHYA PRADESH",
"MAHARASHTRA",
"MANIPUR",
"MEGHALAYA",
"MIZORAM",
"NAGALAND",
"ODISHA",
"PUNJAB",
"RAJASTHAN",
"SIKKIM",
"TAMIL NADU",
# "TELANGANA",
"TRIPURA",
"UTTAR PRADESH",
"UTTARAKHAND",
"WEST BENGAL",
"ANDAMAN AND NICOBAR",
"LAKSHADWEEP",
"PUDUCHERRY"]

def getnthchild(ini, n):
    a = ini
    for i in range(int(n)):
        a = a.find_next_sibling("td")
    return a

def get12sum(ini, n):
    sum = 0
    for i in range(12):
        temp = getnthchild(ini, n+i)
        try:
            sum += float(temp.text)
        except:
            sum += float(temp)
    return sum

filename = sys.argv[1]

eee = [states]



for y in years:
    print("___________________________________", y ,"___________________________________")

    # if y in exclude_years:
        # y = "2017-2018"
    soup = BeautifulSoup(requests.get(base_url1 + y + base_url2).content, 'html.parser')
    print("got 1st url")
    soup2 = BeautifulSoup(requests.get(base_url3 + y + base_url4).content, 'html.parser')
    print("got 2nd url")

    eentries = []
    initial = soup.find_all('td',align='left')
    initial2 = soup2.find_all('td',align='left')
    for st in states:
        print("---------------------",st,"---------------------")
        temp1=None
        temp2=None
        # print(initial1.get_text())
        for elem in initial:
            if elem.get_text().strip() == st:
                temp1 = getnthchild(elem, col1)
        for elem in initial2:
            if elem.get_text().strip() == st:
                # temp1 = getnthchild(elem,col1)
                temp2 = getnthchild(elem,col2)
                # print(elem.get_text())

        if temp1==None or temp2==None:
            # eentries.append(-1)
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            continue
        try:
            print(-1*float(temp1.text), " / ", float(temp2.text), " = ", -1*float(temp1.text)/float(temp2.text))
            eentries.append(-1*float(temp1.text)/float(temp2.text))

        except Exception as e:
            eentries.append(0)

    print(eentries)
    eee.append(eentries)

with open(filename, 'w', newline="") as myfile:
    wr = csv.writer(myfile, delimiter=",")
    for word in np.array(eee).T.tolist():
        wr.writerows([word])

# python cluster.py <num>.csv
