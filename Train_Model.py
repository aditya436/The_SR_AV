# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 23:04:15 2016

@author: aditya
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression

train_m = train.ix[:,['ID','Company_Level','Applicant_Gender',
'Applicant_Marital_Status',
'Applicant_Qualification',
'local',
'product1',
'Manager_Age_Cat',
'Manager_Status'
]]

test_m = test.ix[:,['ID','Company_Level','Applicant_Gender',
'Applicant_Marital_Status',
'Applicant_Qualification',
'local',
'product1',
'Manager_Age_Cat',
'Manager_Status'
]]


#Not improving the score

##'ManagerTotalAgent',
#'ManagerTotalAgentL3',#'Manager_Grade',
#'Applicant_Age_Cat'
#'Manager_Gender'
#'Manager_Current_Designation'
#'Manager_Joining_Designation',
#'Applicant_Occupation',
#'Exp_Mgr',
#'product2',
#'Manager_Business'


train_m.isnull().sum().sort_values()

train_m = train_m.set_index('ID')
target = np.ravel(target)

dummy_df = pd.get_dummies(train_m)

model1 = LogisticRegression()
model1_fit = model1.fit(dummy_df,target)
model1_fit.score(dummy_df,target)

test_m = test_m.set_index('ID')
dummy_test_df = pd.get_dummies(test_m)

predictions = pd.DataFrame(model1_fit.predict(dummy_test_df))
pd.DataFrame.to_csv(predictions,'predictions.csv')

from scipy.stats import spearmanr

rho, pval = spearmanr(target,train_m)

rho_df = pd.DataFrame(rho)

pd.DataFrame.to_csv(rho_df,'rho.csv')

pval = pd.DataFrame(pval)
pd.DataFrame.to_csv(pval,'pval.csv')

list(train_m)

