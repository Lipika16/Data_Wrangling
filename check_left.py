'This person is older than their mother'




'This person is older than their father'

 

'This person has an age difference of less than 10 years with the father.'
'This person has an age difference of less than 10 years with the mother.'
'This person and their mother have an age difference of 50 years or more.'


import pandas as pd
import numpy as np
#org_data = pd.read_excel('Sharma_2018-07-24.xlsx', usecols='E:AJ')
org =  pd.read_excel('../data/sample.xlsx')
org.set_index('IndivID',inplace=True)
def test(i,row):
    mothID = row['MothID']
    if mothID !=0:
        print(i,org['Age'][mothID])
        
for i,row in org.iterrows():
    test(i,row)
'Death year indicated is before birth.'
# -*- coding: utf-8 -*-

'This woman has children with her father. Please check.'
def sim_fath(ind_id,moth_id):
    return (
    (org_data.loc[org_data['IndivID']==ind_id,'FathID'].iloc[0]==
     org_data.loc[org_data['IndivID']==
     moth_id,'FathID'].iloc[0] &
     org_data.loc[org_data['IndivID']==moth_id,'FathID'].iloc[0]!=0
     ))
def fath_is_same(row):
    if row.MothID!=0:
        return sim_fath(row.IndivID,row.MothID)
    else:
        return False
out=org_data.apply(fath_is_same,axis=1)
org_data.loc[out,'FathID']=0
' Father of the individual is set to 0 ' 



'This man has children with his mother, please check.'
def sim_moth(ind_id,fath_id):
    return (
    (org_data.loc[org_data['IndivID']==ind_id,'MothID'].iloc[0]==
     org_data.loc[org_data['IndivID']==
     fath_id,'MothID'].iloc[0] &
     org_data.loc[org_data['IndivID']==fath_id,'MothID'].iloc[0]!=0
     ))
def moth_is_same(row):
    if row.FathID!=0:
        return sim_moth(row.IndivID,row.FathID)
    else:
        return False
output=org_data.apply(moth_is_same,axis=1)
org_data.loc[output,'MothID']=0

' Mother of the individual is set to 0 ' 


'The parents are siblings. Please check.'
def are_siblings(moth_id,fath_id):
    return (
    (org_data.loc[org_data['IndivID']==moth_id,'MothID'].iloc[0]==
     org_data.loc[org_data['IndivID']==fath_id,'MothID'].iloc[0] &
     org_data.loc[org_data['IndivID']==moth_id,'MothID'].iloc[0]!=0
     )
    |
    (org_data.loc[org_data['IndivID']==moth_id,'FathID'].iloc[0]==
     org_data.loc[org_data['IndivID']==fath_id,'FathID'].iloc[0] &
     org_data.loc[org_data['IndivID']==moth_id,'FathID'].iloc[0]!=0))

def parents_are_siblings(row):
    if row.MothID!=0:
        return are_siblings(row.MothID,row.FathID)
    else:
        return False
filtered=org_data.apply(parents_are_siblings,axis=1)
org_data.loc[filtered,'FathID']=0
org_data.loc[filtered,'MothID']=0
