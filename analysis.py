# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:22:13 2018

@author: Lipika Sharma
"""

import pandas as pd 

data_v4=[]
with open('combined.txt','r') as f:
    next(f)
    for line in f:
        data_v4.append(line.split())
columns_v4=['FamID','SessionNum','CalNum','Name','IndivID','Version',
         'Age','BrCaRisk','BrCaRisk%','OvCaRisk','OvCaRisk%']
data_v4=pd.DataFrame(data_v4,columns=columns_v4)
data_v4=data_v4[columns_v4]

out_data_v4=data_v4[['FamID','IndivID','Version','Age','BrCaRisk%','OvCaRisk%']]
#del line
abc=out_data_v4.loc[(out_data_v4['Age']>'70')]
abcd=out_data_v4.loc[(out_data_v4['Age']>'70') & (out_data_v4['BrCaRisk%']<'1.0') ]

lmn=out_data_v4.loc[(out_data_v4['Age']>'70')&(out_data_v4['BrCaRisk%']<'1.0'),'FamID']
lmn = lmn.to_frame().reset_index()


low_risk=all_data[all_data['FamID'].isin(map(str,lmn['FamID']))]
gene=low_risk.loc[(low_risk['Target']==1)]

targets = low_risk.loc[low_risk['Target']==1, ('IndivID')]
tar_mom = low_risk.loc[low_risk['Target']==1, ('MothID')]
tar_fath = low_risk.loc[low_risk['Target']==1, ('FathID')]

mothers = low_risk.loc[(low_risk['Target']==1) & 
                         (low_risk['IndivID'].isin(low_risk['MothID'])), 'IndivID']

mothers = mothers.to_frame().reset_index()
mothers=mothers.rename({'IndivID':'MothID'}, axis='columns')

child=low_risk[low_risk['MothID'].isin(map(str,mothers['MothID']))]
all_child=child['IndivID']


sibling=low_risk[low_risk['MothID'].isin(map(str,list(tar_mom)))]
sibling = sibling.drop(sibling[sibling.MothID == 0].index)
all_sib=sibling['IndivID']


merge=pd.concat([targets,tar_mom,tar_fath, all_child,all_sib], axis=0)
merge=merge.rename("IndivID")

fir_deg_ped=low_risk[low_risk['IndivID'].isin(map(str,list(merge)))]
writer= pd.ExcelWriter('lower_risks.xlsx')
fir_deg_ped.to_excel(writer,'Sheet1')
writer.save()
