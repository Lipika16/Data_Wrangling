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
'BOX-PLOT'
out_data_v4['Age']=out_data_v4['Age'].astype('int64')
out_data_v4['age_range']=pd.cut(out_data_v4['Age'],bins=[20,30,40,50,60,70,80])
out_data_v4['BrCaRisk%']=out_data_v4['BrCaRisk%'].astype('float')

a=out_data_v4[['BrCaRisk%','age_range','IndivID']]
b=a.groupby(['IndivID','age_range'],as_index=False)['BrCaRisk%'].mean()

vx=a[a['IndivID']=='9617']
vr=b[b['IndivID']=='9617']

c = pd.pivot_table(b,values='BrCaRisk%',columns=['age_range'], index=['IndivID'])
fig=c.plot.box(sym='o')
fig.save('plot1')

