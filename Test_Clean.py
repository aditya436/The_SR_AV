# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 00:08:47 2016

@author: aditya
"""

import numpy as np
from dateutil.parser import parse
import dateutil.parser
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

test = pd.read_csv('D:\Projects\The S R\Test.csv')

test['Application_Receipt_Date'] = test['Application_Receipt_Date'].apply(parse)
test['App_Receipt_Month'] = test['Application_Receipt_Date'].dt.month
test.groupby('App_Receipt_Month').ID.nunique().plot()
Q_Res = []
for i in test['App_Receipt_Month']:
    if i <= 3:
        Q_Res.append('Q4')
    elif i <=6:
        Q_Res.append('Q1')
    elif i <=9:
        Q_Res.append('Q2')
    elif i <=12:
        Q_Res.append('Q3')
test['Applied_Quarter'] = Q_Res
del test['Application_Receipt_Date']
del test['App_Receipt_Month']


test.groupby('Office_PIN').ID.nunique().plot()
office = pd.DataFrame(test.groupby('Office_PIN').ID.nunique())
office['Office_PIN'] = office.index

office.columns = ('No_Offices','Office')
adi = pd.DataFrame(office.loc[test['Office_PIN'],'No_Offices'])
adi = adi.reset_index()
test['Tot_Applications'] = adi['No_Offices']
Off_Cat = []
for i in test['Tot_Applications']:
    if i <= 93:
        Off_Cat.append('D')
    elif i <=123:
        Off_Cat.append('C')
    elif i <= 172:
        Off_Cat.append('B')
    elif i <=397:
        Off_Cat.append('A')
test['Company_Level'] = Off_Cat 
del test['Tot_Applications']

test.groupby('Applicant_Gender').ID.nunique()
test['Applicant_Gender'] = test['Applicant_Gender'].fillna('unknown')


test['Applicant_BirthDate'] = test['Applicant_BirthDate'].fillna('7/24/2016')
test['Applicant_BirthDate'] = test['Applicant_BirthDate'].apply(parse)
age_applicant = (datetime.today().date()-test.Applicant_BirthDate)
age_ap = np.ravel(age_applicant)
age_ap = age_ap.astype('timedelta64[D]')
age_int_years = np.int64(age_ap/365)
test['Age_Applicant'] = age_int_years
median = test['Age_Applicant'].median()

Age_app = []
for i in test['Age_Applicant']:
    if i == 0:
        Age_app.append(38)
    else:
        Age_app.append(i)
test['Age_Applicant'] = Age_app
age = []
test['Age_Applicant'].describe()
test['Age_Applicant'].mean()
for i in test['Age_Applicant']:
    if i <=33 :
        age.append('L33')
    elif i <= 38 :
        age.append('L38')
    elif i < 65 :
        age.append('L46')
    elif i >=65 :
        age.append('L86')
pd.DataFrame.to_csv(test,'test.csv')
age = pd.DataFrame(age)

test['Applicant_Age_Cat'] = age

test['Applicant_City_PIN'] = test['Applicant_City_PIN'].fillna('Missing')

local = []
for i in test.index:
    if test.Applicant_City_PIN[i] == test.Office_PIN[i]:
        local.append('Local')
    elif test.Applicant_City_PIN[i] == 'Missing':
        local.append('Missing')
    else:
        local.append('Non_local')
        
test['local'] = local

test['Manager_Grade'] = test['Manager_Grade'].fillna('Direct')
test['Manager_Current_Designation'] = test['Manager_Current_Designation'].fillna('Direct')
test['Manager_Status'] = test['Manager_Status'].fillna('Direct')
test['Manager_Gender'] = test['Manager_Gender'].fillna('Direct')

test['Manager_Joining_Designation'] = test['Manager_Joining_Designation'].fillna('Direct')
test.groupby('Manager_Joining_Designation').ID.nunique()

current_d = []
for i in test.index:
    if test.Manager_Joining_Designation[i] == 'Level 6':
        current_d.append('Level 5')
    elif test.Manager_Joining_Designation[i] == 'Level 7':
        current_d.append('Level 5')
    elif test.Manager_Joining_Designation[i] == 'Level 5':
        current_d.append('Level 5')
    elif test.Manager_Joining_Designation[i] == 'Level 4':
        current_d.append('Level 4')
    elif test.Manager_Joining_Designation[i] == 'Level 3':
        current_d.append('Level 3')
    elif test.Manager_Joining_Designation[i] == 'Level 2':
        current_d.append('Level 2')
    elif test.Manager_Joining_Designation[i] == 'Level 1':
        current_d.append('Level 1')
    else: 
        current_d.append('Direct')
    
test['Manager_Joining_Designation'] = current_d

#Manager_Grade Feature

test['Manager_Grade'] = test['Manager_Grade'].fillna('Direct')
grade = []
for i in test.index:
    if test.Manager_Grade[i] <= 2:
        grade.append('L2')
    elif test.Manager_Grade[i] == 3:
        grade.append('L3')
    elif test.Manager_Grade[i] <= 5:
        grade.append('L5')
    elif test.Manager_Grade[i] <= 10:
        grade.append('L10')  
    else: 
        grade.append('Direct')
test['Manager_Grade'] = grade

#Applicant_Occupation feature

test['Applicant_Occupation'] = test['Applicant_Occupation'].fillna('Others')
test.groupby('Applicant_Occupation').ID.nunique()


#Managers Age

test['Manager_DoB'] = test['Manager_DoB'].fillna('7/24/2016')
test['Manager_DoB'] = test['Manager_DoB'].apply(parse)
age_manager = (datetime.today().date()-test.Manager_DoB)
age_mgr = np.ravel(age_manager)
age_mgr = age_mgr.astype('timedelta64[D]')
age_int_years = np.int64(age_mgr/365)
test['Age_Manager'] = age_int_years
test['Age_Manager'].median()
Age_man = []
for i in test['Age_Manager']:
    if i == 0:
        Age_man.append(42)
    else:
        Age_man.append(i)
test['Age_Manager'] = Age_man
test.groupby('Age_Manager').ID.nunique()
test['Age_Manager'].describe
age = []
for i in test['Age_Manager']:
    if i <=35 :
        age.append('L35')
    elif i <= 40 :
        age.append('L40')
    elif i <= 45 :
        age.append('L45')
    elif i <=50 :
        age.append('L50')
    elif i <=55 :
        age.append('L55')
    elif i <=60 :
        age.append('L60')
    else:
        age.append('G60')

test['Manager_Age_Cat'] = age


#Managers Experience in years

test['Manager_DOJ'] = test['Manager_DOJ'].fillna('7/24/2016')
test['Manager_DOJ'] = test['Manager_DOJ'].apply(parse)
exp_manager = (datetime.today().date()-test.Manager_DOJ)
exp_mgr = np.ravel(exp_manager)
exp_mgr = exp_mgr.astype('timedelta64[D]')
exp_int_years = np.int64(exp_mgr/365)
test['Exp_Manager'] = exp_int_years
test['Exp_Manager'].median()
Exp_man = []
for i in test['Exp_Manager']:
    if i == 0:
        Exp_man.append(9)
    else:
        Exp_man.append(i)
test['Exp_Manager'] = Exp_man
test.groupby('Exp_Manager').ID.nunique()

exp = []

for i in test['Exp_Manager']:
    if i <=10 :
        exp.append('L10')
    elif i <=12 :
        exp.append('L12')
    elif i <=14 :
        exp.append('L14')
    else:
        exp.append('G14')
    
test['Exp_Mgr'] = exp

#Manager No_of Producsts feature
test['Manager_Num_Products'].median()
test['Manager_Num_Products'] = test['Manager_Num_Products'].fillna(2)
test.Manager_Num_Products.describe()
test.groupby('Manager_Num_Products').ID.nunique()

pro = []

for i in test['Manager_Num_Products']:
    if i == 0 :
        pro.append('NoSale')
    elif i <=4 :
        pro.append('L4')
    elif i == 5 :
        pro.append('L5')
    elif i <=15 :
        pro.append('L15')
    elif i <=25 :
        pro.append('L25')
    elif i <=40 :
        pro.append('L40')
    else:
        pro.append('G40')

test['product1'] = pro

#Manager No_of Producsts feature in last 3 months

test.Manager_Num_Products2.describe()
test.groupby('Manager_Num_Products2').ID.nunique()
test['Manager_Num_Products2'] = test['Manager_Num_Products2'].fillna(5)

pro = []
for i in test['Manager_Num_Products2']:
    if i == 0 :
        pro.append('NoSale')
    elif i <=4 :
        pro.append('L4')
    elif i == 5 :
        pro.append('L5')
    elif i <=10 :
        pro.append('L10')
    elif i <=15 :
        pro.append('L15')
    else:
        pro.append('G15')

test['product2'] = pro


## Number of agents sourced by Manager

test.Manager_Num_Application.describe()
test.groupby('Manager_Num_Application').ID.nunique()
test['Manager_Num_Application'] = test['Manager_Num_Application'].fillna(2)

pro = []

for i in test['Manager_Num_Application']:
    if i == 0 :
        pro.append('None')
    elif i == 1 :
        pro.append('One')
    elif i == 2 :
        pro.append('Two')
    elif i == 3 :
        pro.append('Three')
    elif i <= 5 :
        pro.append('L5')
    elif i <= 10 :
        pro.append('L10')
    else:
        pro.append('G10')

test['ManagerTotalAgent'] = pro

test.groupby('ManagerTotalAgent').ID.nunique()


## Number of agents sourced by Manager in last 3 months

test.Manager_Num_Coded.describe()
test.groupby('Manager_Num_Coded').ID.nunique()
test['Manager_Num_Coded'] = test['Manager_Num_Coded'].fillna(1)

pro = []

for i in test['Manager_Num_Coded']:
    if i == 0 :
        pro.append('None')
    elif i == 1 :
        pro.append('One')
    elif i == 2 :
        pro.append('Two')
    elif i <= 4 :
        pro.append('L4')
    else:
        pro.append('G4')

test['ManagerTotalAgentL3'] = pro

test.groupby('ManagerTotalAgentL3').ID.nunique()

## Manager business last 3 months

test.Manager_Business.mean()
test.Manager_Business.describe()
test.groupby('Manager_Business').ID.nunique()
test['Manager_Business'] = test['Manager_Business'].fillna(111575)
test['Manager_Business'] = abs(test['Manager_Business'])

pro = []

for i in test['Manager_Business']:
    if i == 0 :
        pro.append('No_business')
    elif i <= 100000 :
        pro.append('L1')
    elif i <= 500000 :
        pro.append('L5')
    elif i <= 1000000 :
        pro.append('L10')
    elif i <= 1500000 :
        pro.append('L15')   
    else:
        pro.append('G15')

test['Manager_Business'] = pro

test.groupby('Manager_Business').ID.nunique()

#Applicant Qualification feature

test.groupby('Applicant_Qualification').ID.nunique()
test['Applicant_Qualification'] = test['Applicant_Qualification'].fillna('unknown')
qual = pd.DataFrame(test.groupby('Applicant_Qualification').ID.nunique())

qual = qual.reset_index()

qual0 = qual.Applicant_Qualification[0]
qual1 = qual.Applicant_Qualification[1]
qual2 = qual.Applicant_Qualification[2]
qual3 = qual.Applicant_Qualification[3]
qual4 = qual.Applicant_Qualification[4]
qual5 = qual.Applicant_Qualification[5]
qual6 = qual.Applicant_Qualification[6]
qual7 = qual.Applicant_Qualification[7]
qual8 = qual.Applicant_Qualification[8]

test['Applicant_Qualification1'] = test['Applicant_Qualification'] 


qualific = []

for i in test['Applicant_Qualification']:
    if i == qual0 :
        qualific.append('Prof_Q')    
    elif i == qual1 :
        qualific.append('Prof_Q')
    elif i == qual7 :
        qualific.append('Prof_Q')
    elif i == qual2 :
        qualific.append(qual2)
    elif i == qual3 :
        qualific.append(qual3)
    elif i == qual4 :
        qualific.append(qual4)
    elif i == qual5 :
        qualific.append(qual5)
    elif i == qual6 :
        qualific.append(qual6)
    elif i == qual8 :
        qualific.append(qual8)

test['Applicant_Qualification'] = qualific

