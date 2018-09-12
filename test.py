import pandas as pd
#import numpy as np
from clean import Clean
#org_data = pd.read_excel('Sharma_2018-07-24.xlsx', usecols='E:AJ')
org_data= pd.read_excel('../data/all_data.xlsx', usecols='E:AJ')
backup_data=org_data
clean = Clean(org_data)
clean.clean_data()
org_data = clean.org_data

'This woman has children with her father. Please check.'
def sim_fath(ind_id,moth_id):
    return (
    (org_data.loc[org_data['IndivID']==ind_id,'FathID'].iloc[0]==org_data.loc[org_data['IndivID']==
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
    (org_data.loc[org_data['IndivID']==ind_id,'MothID'].iloc[0]==org_data.loc[org_data['IndivID']==
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


'This family has no probands.'

