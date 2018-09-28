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

mer=pd.concat([out_data_v4,v3], axis=1)

mer=mer.drop(['OvCaRisk%', 'OvCaRisk2'], axis=1)

mer2['Age']=mer2['Age'].astype('int64')
mer2['age_range']=pd.cut(mer2['Age'],bins=[20,30,40,50,60,70,80])
mer2['BrCaRisk%']=mer2['BrCaRisk%'].astype('float')

mer2['Version'] = mer2['Version'].str.replace('v3','version3')
mer2['Version'] = mer2['Version'].str.replace('v4beta14','version4')

from openpyxl import Workbook

writer= pd.ExcelWriter('risks_versions.xlsx')
mer.to_excel(writer,'Sheet1')
writer.save()

#k = pd.pivot_table(all_risks,values='BrCaRisk%',columns=['age_range'], index=['IndivID'])

sns.catplot(x="age_range", y="BrCaRisk%", hue="Status",
            kind="violin", split=True, data=mer, palette="Set2");
plt.savefig('affec.png',dpi=500)      
        
bx = sns.boxplot(x="age_range", y="BrCaRisk%", hue="Version",
                  data=mer1, palette='bright', sym='').set_title('CHEK2')
plt.savefig('BOX_CHEK.png',dpi=500)

mer=pd.concat([palb_risk_v3,palb_risk], axis=0)

mer1=pd.concat([chek_risk_v3,chek_risk], axis=0)

mer2=pd.concat([atm_risk_v3,atm_risk], axis=0)
