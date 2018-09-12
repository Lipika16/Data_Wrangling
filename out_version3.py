# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:48:21 2018

@author: Lipika Sharma
"""
import pandas as pd
data_v3=[]
with open('../combined_v3.txt','r') as f:
    next(f)
    for line in f:
        data_v3.append(line.split())
columns_v3=['FamID','Date','Time','SessionNum','CalNum','Name','IndivID','Version',
         'Age','BrCaRisk','BrCaRisk%','OvCaRisk','OvCaRisk%']
data_v3=pd.DataFrame(data_v3,columns=columns_v3)
data_v3=data_v3[columns_v3]

out_data_v3=data_v3[['FamID','IndivID','Version','Age','BrCaRisk%','OvCaRisk%']]

