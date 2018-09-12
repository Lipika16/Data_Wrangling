# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:22:13 2018

@author: Lipika Sharma
"""


data_v4=[]
with open('../combined.txt','r') as f:
    next(f)
    for line in f:
        data_v4.append(line.split())
columns_v4=['FamID','SessionNum','CalNum','Name','IndivID','Version',
         'Age','BrCaRisk','BrCaRisk%','OvCaRisk','OvCaRisk%']
data_v4=pd.DataFrame(data_v4,columns=columns_v4)
data_v4=data_v4[columns_v4]

out_data_v4=data_v4[['FamID','IndivID','Version','Age','BrCaRisk%','OvCaRisk%']]

import matplotlib.pyplot as  plt
x=out_data_v4.loc[out_data_v4['FamID']=='AAAFC631', 'Age']
y=out_data_v4.loc[out_data_v4['FamID']=='AAAFC631', 'BrCaRisk%']
plt.plot(x,y)
plt.show()





#del line
#columns=['FamID','Date','Time','SessionNum','CalNum','Name','IndivID','Version',
#         'Age','BrCaRisk','BrCaRisk%','OvCaRisk','OvCaRisk%']
