# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 08:38:52 2016

@author: aditya
"""
import numpy as np
from dateutil.parser import parse
import dateutil.parser
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date
import pandas as pd

train = pd.read_csv('D:\Projects\The S R\Train.csv')

target = train['Business_Sourced']
del train['Business_Sourced']

train.groupby('Office_PIN').ID.nunique().plot()
office = pd.DataFrame(train.groupby('Office_PIN').ID.nunique())
office['Office_PIN'] = office.index

office.columns = ('No_Offices','Office')
adi = pd.DataFrame(office.loc[train['Office_PIN'],'No_Offices'])
adi = adi.reset_index()
train['Tot_Applications'] = adi['No_Offices']
Off_Cat = []
for i in train['Tot_Applications']:
    if i <= 93:
        Off_Cat.append('D')
    elif i <=123:
        Off_Cat.append('C')
    elif i <= 172:
        Off_Cat.append('B')
    elif i <=397:
        Off_Cat.append('A')
train['Company_Level'] = Off_Cat 
del train['Tot_Applications']


train.groupby('Applicant_Gender').ID.nunique()
train['Applicant_Gender'] = train['Applicant_Gender'].fillna('unknown')

train.groupby('Applicant_Marital_Status').ID.nunique()
train['Applicant_Marital_Status'] = train['Applicant_Marital_Status'].fillna('unknown')

train.groupby('Applicant_Qualification').ID.nunique()
train['Applicant_Qualification'] = train['Applicant_Qualification'].fillna('unknown')
qual = pd.DataFrame(train.groupby('Applicant_Qualification').ID.nunique())

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
qual9 = qual.Applicant_Qualification[9]
qual10 = qual.Applicant_Qualification[10]

train['Applicant_Qualification1'] = train['Applicant_Qualification'] 

train.groupby('Applicant_Qualification1').ID.nunique()

qualific = []

for i in train['Applicant_Qualification']:
    if i == qual0 :
        qualific.append('Prof_Q')    
    elif i == qual1 :
        qualific.append('Prof_Q')
    elif i == qual2 :
        qualific.append('Prof_Q')
    elif i == qual3 :
        qualific.append('Prof_Q')
    elif i == qual4 :
        qualific.append('Prof_Q')
    elif i == qual10 :
        qualific.append('Prof_Q')
    elif i == qual5 :
        qualific.append(qual5)
    elif i == qual6 :
        qualific.append(qual6)
    elif i == qual7 :
        qualific.append(qual7)
    elif i == qual8 :
        qualific.append(qual8)
    elif i == qual9 :
        qualific.append(qual9)
    else: 
        qualific.append('Unknown')
    
train['Applicant_Qualification'] = qualific

#Applicant's Age feature

train['Applicant_BirthDate'] = train['Applicant_BirthDate'].fillna('7/24/2016')
train['Applicant_BirthDate'] = train['Applicant_BirthDate'].apply(parse)
age_applicant = (datetime.today().date()-train.Applicant_BirthDate)
age_ap = np.ravel(age_applicant)
age_ap = age_ap.astype('timedelta64[D]')
age_int_years = np.int64(age_ap/365)
train['Age_Applicant'] = age_int_years
train['Age_Applicant'].median()
Age_app = []
for i in train['Age_Applicant']:
    if i == 0:
        Age_app.append(38)
    else:
        Age_app.append(i)
train['Age_Applicant'] = Age_app
age = []
for i in train['Age_Applicant']:
    if i <=33 :
        age.append('L33')
    elif i <= 38 :
        age.append('L38')
    elif i < 46 :
        age.append('L46')
    elif i <=86 :
        age.append('L86')
train['Applicant_Age_Cat'] = age

## feature : Local

train['Applicant_City_PIN'] = train['Applicant_City_PIN'].fillna('Missing')

local = []
for i in train.index:
    if train.Applicant_City_PIN[i] == train.Office_PIN[i]:
        local.append('Local')
    elif train.Applicant_City_PIN[i] == 'Missing':
        local.append('Missing')
    else:
        local.append('Non_local')
        
train['local'] = local
        
## feature : Manager_Exp : Will take a little time
        
train['Manager_Current_Designation'] = train['Manager_Current_Designation'].fillna('Direct')
train['Manager_Status'] = train['Manager_Status'].fillna('Direct')
train['Manager_Gender'] = train['Manager_Gender'].fillna('Direct')
        
train['Manager_Joining_Designation'] = train['Manager_Joining_Designation'].fillna('Direct')
train.groupby('Manager_Joining_Designation').ID.nunique()

current_d = []
for i in train.index:
    if train.Manager_Joining_Designation[i] == 'Level 6':
        current_d.append('Level 5')
    elif train.Manager_Joining_Designation[i] == 'Level 7':
        current_d.append('Level 5')
    elif train.Manager_Joining_Designation[i] == 'Level 5':
        current_d.append('Level 5')
    elif train.Manager_Joining_Designation[i] == 'Level 4':
        current_d.append('Level 4')
    elif train.Manager_Joining_Designation[i] == 'Level 3':
        current_d.append('Level 3')
    elif train.Manager_Joining_Designation[i] == 'Level 2':
        current_d.append('Level 2')
    elif train.Manager_Joining_Designation[i] == 'Level 1':
        current_d.append('Level 1')
    else: 
        current_d.append('Direct')
    
train['Manager_Joining_Designation'] = current_d    

#Manager Grade feature

train['Manager_Grade'] = train['Manager_Grade'].fillna('Direct')
grade = []
for i in train.index:
    if train.Manager_Grade[i] <= 2:
        grade.append('L2')
    elif train.Manager_Grade[i] == 3:
        grade.append('L3')
    elif train.Manager_Grade[i] <= 5:
        grade.append('L5')
    elif train.Manager_Grade[i] <= 10:
        grade.append('L10')  
    else: 
        grade.append('Direct')
train['Manager_Grade'] = grade

#Applicant_Occupation feature

train['Applicant_Occupation'] = train['Applicant_Occupation'].fillna('Others')
train.groupby('Applicant_Occupation').ID.nunique()

#Managers Age

train['Manager_DoB'] = train['Manager_DoB'].fillna('7/24/2016')
train['Manager_DoB'] = train['Manager_DoB'].apply(parse)
age_manager = (datetime.today().date()-train.Manager_DoB)
age_mgr = np.ravel(age_manager)
age_mgr = age_mgr.astype('timedelta64[D]')
age_int_years = np.int64(age_mgr/365)
train['Age_Manager'] = age_int_years
train['Age_Manager'].median()
Age_man = []
for i in train['Age_Manager']:
    if i == 0:
        Age_man.append(42)
    else:
        Age_man.append(i)
train['Age_Manager'] = Age_man
train.groupby('Age_Manager').ID.nunique()
train['Age_Manager'].describe
age = []
for i in train['Age_Manager']:
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

train['Manager_Age_Cat'] = age

#Managers Experience in years

train['Manager_DOJ'] = train['Manager_DOJ'].fillna('7/24/2016')
train['Manager_DOJ'] = train['Manager_DOJ'].apply(parse)
exp_manager = (datetime.today().date()-train.Manager_DOJ)
exp_mgr = np.ravel(exp_manager)
exp_mgr = exp_mgr.astype('timedelta64[D]')
exp_int_years = np.int64(exp_mgr/365)
train['Exp_Manager'] = exp_int_years
train['Exp_Manager'].median()
Exp_man = []
for i in train['Exp_Manager']:
    if i == 0:
        Exp_man.append(9)
    else:
        Exp_man.append(i)
train['Exp_Manager'] = Exp_man
train.groupby('Exp_Manager').ID.nunique()


exp = []

for i in train['Exp_Manager']:
    if i <=10 :
        exp.append('L10')
    elif i <=12 :
        exp.append('L12')
    elif i <=14 :
        exp.append('L14')
    else:
        exp.append('G14')
    
train['Exp_Mgr'] = exp

#Manager No_of Producsts feature

train.Manager_Num_Products.describe()
train.groupby('Manager_Num_Products').ID.nunique()
train['Manager_Num_Products'] = train['Manager_Num_Products'].fillna(5)

pro = []

for i in train['Manager_Num_Products']:
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

train['product1'] = pro

#Manager No_of Producsts feature in last 3 months

train.Manager_Num_Products2.describe()
train.groupby('Manager_Num_Products2').ID.nunique()
train['Manager_Num_Products2'] = train['Manager_Num_Products2'].fillna(5)

pro = []

for i in train['Manager_Num_Products2']:
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

train['product2'] = pro

## Number of agents sourced by Manager

train.Manager_Num_Application.describe()
train.groupby('Manager_Num_Application').ID.nunique()
train['Manager_Num_Application'] = train['Manager_Num_Application'].fillna(1)

pro = []

for i in train['Manager_Num_Application']:
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

train['ManagerTotalAgent'] = pro

train.groupby('ManagerTotalAgent').ID.nunique()

## Number of agents sourced by Manager in last 3 months

train.Manager_Num_Coded.describe()
train.groupby('Manager_Num_Coded').ID.nunique()
train['Manager_Num_Coded'] = train['Manager_Num_Coded'].fillna(0)

pro = []

for i in train['Manager_Num_Coded']:
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

train['ManagerTotalAgentL3'] = pro

train.groupby('ManagerTotalAgentL3').ID.nunique()

## Manager business last 3 months

train.Manager_Business.mean()
train.Manager_Business.describe()
train.groupby('Manager_Business').ID.nunique()
train['Manager_Business'] = train['Manager_Business'].fillna(184371)
train['Manager_Business'] = abs(train['Manager_Business'])

pro = []

for i in train['Manager_Business']:
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

train['Manager_Business'] = pro

train.groupby('Manager_Business').ID.nunique()

