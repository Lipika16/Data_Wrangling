# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:19:07 2018

@author: Lipika Sharma
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

all_data = pd.read_excel('data/cleaned_data.xlsx')

#risks for unaffected individuaks computed by version 4
data_all=[]
with open('data/all_genes_risk.txt','r') as f:
    next(f)
    for line in f:
        data_all.append(line.split())
columns_all=['FamID','SessionNum','CalNum','Name','IndivID','Version',
         'Age','BrCaRisk','BrCaRisk%','OvCaRisk','OvCaRisk%']
data_all=pd.DataFrame(data_all,columns=columns_all)
data_all=data_all[columns_all]

all_data_v4=data_all[['FamID','IndivID','Version','Age','BrCaRisk%','OvCaRisk%']]

#risks for unaffected individuaks computed by version 3
data_v3=[]
with open('data/all_genesv3_risks.txt','r') as f:
    next(f)
    for line in f:
        data_v3.append(line.split())
columns_v3=['FamID','Date','Time','SessionNum','CalNum','Name','IndivID','Version',
         'Age','BrCaRisk','BrCaRisk%','OvCaRisk','OvCaRisk%']
data_v3=pd.DataFrame(data_v3,columns=columns_v3)
data_v3=data_v3[columns_v3]
out_data_v3=data_v3[['FamID','IndivID','Version','Age','BrCaRisk%','OvCaRisk%']]

#unaffected mutation carriers for these three genes
palb_ind=all_data.loc[(all_data['PALB2r']=='P')&(all_data['Target']==1),'IndivID']
chek_ind=all_data.loc[(all_data['CHEK2r']=='P')&(all_data['Target']==1),'IndivID']
atm_ind=all_data.loc[(all_data['ATMr']=='P')&(all_data['Target']==1),'IndivID']

#just work for PALB2 
#version 4
palb_risk_v4=all_data_v4[all_data_v4['IndivID'].isin(map(str,list(palb_ind)))]
palb_risk_v4['Age']=palb_risk_v4['Age'].astype('int64')
palb_risk_v4['age_range']=pd.cut(palb_risk_v4['Age'],bins=[20,30,40,50,60,70,80])
palb_risk_v4['BrCaRisk%']=palb_risk_v4['BrCaRisk%'].astype('float')


#version 3
palb_risk_v3=out_data_v3[out_data_v3['IndivID'].isin(map(str,list(palb_ind)))]
palb_risk_v3['Age']=palb_risk_v3['Age'].astype('int64')
palb_risk_v3['age_range']=pd.cut(palb_risk_v3['Age'],bins=[20,30,40,50,60,70,80])
palb_risk_v3['BrCaRisk%']=palb_risk_v3['BrCaRisk%'].astype('float')



#Line plots for both
indiv_lines = pd.pivot_table(palb_risk_v4,values='BrCaRisk%',columns=['Age'],index='IndivID')
indiv_lines_v3 = pd.pivot_table(palb_risk_v3,values='BrCaRisk%',columns=['Age'],index='IndivID')



for row in indiv_lines.values:
    xs = []
    ys = []
    for i,j in zip(row,indiv_lines.columns):
        if i>0:
            xs.append(j)
            ys.append(i)
    plt.plot(xs,ys,'-+')
for row in indiv_lines_v3.values:
    xs = []
    ys = []
    for i,j in zip(row,indiv_lines_v3.columns):
        if i>0:
            xs.append(j)
            ys.append(i)
    plt.plot(xs,ys,'-o')

plt.savefig('linePlotBoth.png',dpi=500)
plt.close()
plt.show()

#mean for the boxplot
mean_plot = pd.pivot_table(palb_risk_v4,values='BrCaRisk%',columns=['age_range'],index='IndivID')
bx = sns.boxplot(x=mean_plot.columns,
                  data=mean_plot,palette='colorblind')
color = dict(boxes='DarkGreen', whiskers='DarkOrange',medians='DarkBlue', caps='Gray')
mean_plot.plot.box(color=color)
mean_plot_v3.plot.box(color=color)

mean_plot_v3=pd.pivot_table(palb_risk_v3,values='BrCaRisk%',columns=['age_range'],index='IndivID')
color = dict(boxes='DarkGreen', whiskers='DarkOrange',medians='DarkBlue', caps='Gray')
mean_plot_v3.plot.box(color=color)

fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(mean_plot_v3.values)

stress1=palb_risk_v4.groupby(['IndivID','Version','age_range'],as_index=False)['BrCaRisk%'].mean()
stress2=palb_risk_v3.groupby(['IndivID','Version','age_range'],as_index=False)['BrCaRisk%'].mean()
mer=pd.concat([stress2,stress1], axis=0)
bx = sns.boxplot(x="age_range", y="BrCaRisk%",hue='Version',
                  data=mer,palette='colorblind', sym='')
bx.set(xlabel='Age Range', ylabel='Risk')
plt.savefig('BoxPlot13.png',dpi=500)

