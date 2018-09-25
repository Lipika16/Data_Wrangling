# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:57:41 2018

@author: Lipika Sharma
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#all_risks= pd.read_excel('../data/risks.xlsx')
v3=out_data_v3[out_data_v3['IndivID'].isin(map(str,out_data_v4['IndivID']))]

mer=pd.concat([v3, out_data_v4], axis=0)

mer['Age']=mer['Age'].astype('int64')
mer['age_range']=pd.cut(mer['Age'],bins=[20,30,40,50,60,70,80])
mer['BrCaRisk%']=mer['BrCaRisk%'].astype('float')

mer['Version'] = mer['Version'].str.replace('v3','version3')
mer['Version'] = mer['Version'].str.replace('v4beta14','version4')

#k = pd.pivot_table(all_risks,values='BrCaRisk%',columns=['age_range'], index=['IndivID'])

ax = sns.boxplot(x=("age_range"), y="BrCaRisk%", hue="Version",
                  data=mer, palette="muted",sym='')
plt.savefig('boxplot.png',dpi=500)
plt.close()

bx = sns.violinplot(x="age_range", y="BrCaRisk%", hue="Version",
                  data=mer, palette="muted")
plt.savefig('violinplot.png',dpi=500)