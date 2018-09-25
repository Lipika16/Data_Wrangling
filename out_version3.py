# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:48:21 2018

@author: Lipika Sharma
"""

import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
data_v3=[]
with open('combined_v3.txt','r') as f:
    next(f)
    for line in f:
        data_v3.append(line.split())
columns_v3=['FamID','Date','Time','SessionNum','CalNum','Name','IndivID','Version',
         'Age','BrCaRisk','BrCaRisk%','OvCaRisk','OvCaRisk%']
data_v3=pd.DataFrame(data_v3,columns=columns_v3)
data_v3=data_v3[columns_v3]

out_data_v3=data_v3[['FamID','IndivID','Version','Age','BrCaRisk%','OvCaRisk%']]
out_data_v3=out_data_v3.rename({'FamID':'FamID2','IndivID':'IndivID2', 'Age':'Age2',
                        'Version':'Version2', 'BrCaRisk%':'BrCaRisk%2', 'OvCaRisk%':'OvCaRisk2'
                              }, axis='columns')

#del line
'BOX PLOT'
out_data_v3['Age2']=out_data_v3['Age2'].astype('int64')
out_data_v3['age_bins']=pd.cut(out_data_v3['Age2'],bins=[20,30,40,50,60,70,80])
out_data_v3['BrCaRisk%2']=out_data_v3['BrCaRisk%2'].astype('float')

x=out_data_v3[['BrCaRisk%2','age_bins','IndivID2']]

r=x.groupby(['IndivID2','age_bins'],as_index=False)['BrCaRisk%2'].mean()
vx=x[x['IndivID2']=='9617']
vr=r[r['IndivID2']=='9617']

y = pd.pivot_table(r,values='BrCaRisk%2',columns=['age_bins'], index=['IndivID2'])
fig=y.plot.box(sym='o')
