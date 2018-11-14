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

v3['Age']=v3['Age'].astype('int64')
v3['age_range']=pd.cut(v3['Age'],bins=[20,30,40,50,60,70,80])
v3['BrCaRisk%']=v3['BrCaRisk%'].astype('float')
v3_transf = pd.pivot_table(v3,values='BrCaRisk%',columns=['age_range'],index='IndivID')
v3_transf.median()
v3_statistics=v3_transf.describe()

mer=pd.concat([v3,out_data_v4], axis=0)

mer=mer.drop(['OvCaRisk%'], axis=1)

mer['Age']=mer['Age'].astype('int64')
mer['age_range']=pd.cut(mer['Age'],bins=[20,30,40,50,60,70,80])
mer['BrCaRisk%']=mer['BrCaRisk%'].astype('float')

mer['Version'] = mer['Version'].str.replace('v3','version3')
mer['Version'] = mer['Version'].str.replace('v4beta14','version4')

bx = sns.boxplot(x="age_range", y="BrCaRisk%", hue="Version",
                  data=mer,palette='colorblind', sym='').set_title('Distribution of Breast Cancer Risks based on Version 3 and Version 4 ')
plt.savefig('thesis_allrisks',dpi=500)


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




out_data_v4['Age']=out_data_v4['Age'].astype('int64')
out_data_v4['age_range']=pd.cut(out_data_v4['Age'],bins=[20,30,40,50,60,70,80])
out_data_v4['BrCaRisk%']=out_data_v4['BrCaRisk%'].astype('float')
v4_trans = pd.pivot_table(out_data_v4,values='BrCaRisk%',columns=['age_range'],index='IndivID')
v4_trans.median()
v4_stats=v4_trans.describe()
