# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:22:43 2018

@author: Lipika Sharma
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

all_data = pd.read_excel('data/cleaned_data.xlsx')

#extracting all the unaffected individuals 
non_affec=all_data.loc[(all_data['Target']==1)&(all_data['1stBrCa']==0)]


#version 4
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
b=all_data_v4['IndivID'].unique()


#version3
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

a=out_data_v3['IndivID'].unique()

palb_ind=all_data.loc[(all_data['PALB2r']=='P')&(all_data['Target']==1),'IndivID']
chek_ind=all_data.loc[(all_data['CHEK2r']=='P')&(all_data['Target']==1),'IndivID']
atm_ind=all_data.loc[(all_data['ATMr']=='P')&(all_data['Target']==1),'IndivID']

#for version 4
palb_risk_v4=all_data_v4[all_data_v4['IndivID'].isin(map(str,list(palb_ind)))]
writer = pd.ExcelWriter('plab_risks_v4.xlsx')
palb_risk_v4.to_excel(writer,'Sheet1')
writer.save()
    
chek_risk_v4=all_data_v4[all_data_v4['IndivID'].isin(map(str,list(chek_ind)))]
writer = pd.ExcelWriter('chek_risk_v4.xlsx')
chek_risk_v4.to_excel(writer,'Sheet1')
writer.save()

atm_risk_v4=all_data_v4[all_data_v4['IndivID'].isin(map(str,list(atm_ind)))]
writer = pd.ExcelWriter('atm_risks_v4.xlsx')
atm_risk_v4.to_excel(writer,'Sheet1')
writer.save()

#for version 3
palb_risk_v3=out_data_v3[out_data_v3['IndivID'].isin(map(str,list(palb_ind)))]
chek_risk_v3=out_data_v3[out_data_v3['IndivID'].isin(map(str,list(chek_ind)))]
atm_risk_v3=out_data_v3[out_data_v3['IndivID'].isin(map(str,list(atm_ind)))]


#for gene ATM
mer_atm=pd.concat([atm_risk_v3,atm_risk_v4], axis=0)
mer_atm=mer_atm.drop(['OvCaRisk%', 'OvCaRisk%'], axis=1)

mer_atm['Age']=mer_atm['Age'].astype('int64')
mer_atm['age_range']=pd.cut(mer_atm['Age'],bins=[20,30,40,50,60,70,80])
mer_atm['BrCaRisk%']=mer_atm['BrCaRisk%'].astype('float')

mer_atm['Version'] = mer_atm['Version'].str.replace('v3','version3')
mer_atm['Version'] = mer_atm['Version'].str.replace('v4beta14','version4')

bx = sns.boxplot(x="age_range", y="BrCaRisk%", hue="Version",
                  data=mer_atm,palette='colorblind', sym='').set_title('ATM')
plt.savefig('updated_ATM.png',dpi=500)

#descriptive statistics for version 3 (ATM)
atm_risk_v4['Age']=atm_risk_v4['Age'].astype('int64')
atm_risk_v4['age_range']=pd.cut(atm_risk_v4['Age'],bins=[20,30,40,50,60,70,80])
atm_risk_v3['BrCaRisk%']=atm_risk_v3['BrCaRisk%'].astype('float')
r = pd.pivot_table(atm_risk_v3,values='BrCaRisk%',columns=['age_range'],index='IndivID')
stats_atm=r.describe()

#for gene PALB2
mer_atm=pd.concat([atm_risk_v3,atm_risk_v4], axis=0)
mer_palb2=pd.concat([palb_risk_v3,palb_risk_v4], axis=0)
mer_palb2=mer_palb2.drop(['OvCaRisk%', 'OvCaRisk%'], axis=1)

mer_palb2['Age']=mer_palb2['Age'].astype('int64')
mer_palb2['age_range']=pd.cut(mer_palb2['Age'],bins=[20,30,40,50,60,70,80])
mer_palb2['BrCaRisk%']=mer_palb2['BrCaRisk%'].astype('float')

mer_palb2['Version'] = mer_palb2['Version'].str.replace('v3','version3')
mer_palb2['Version'] = mer_palb2['Version'].str.replace('v4beta14','version4')

bx = sns.boxplot(x="age_range", y="BrCaRisk%", hue="Version",
                  data=mer_palb2,palette='colorblind', sym='').set_title('PALB2')
plt.savefig('updated_PALB2.png',dpi=500)

#descriptive statistics for version 3 (PALB2)
palb_risk_v4['Age']=palb_risk_v4['Age'].astype('int64')
palb_risk_v4['age_range']=pd.cut(palb_risk_v4['Age'],bins=[20,30,40,50,60,70,80])
palb_risk_v4['BrCaRisk%']=palb_risk_v4['BrCaRisk%'].astype('float')
r = pd.pivot_table(palb_risk_v4,values='BrCaRisk%',columns=['age_range'],index='IndivID')

pal_xcel = pd.read_excel('data/palb_risks.xlsx')
pal_xcel = pal_xcel.set_index(['IndivID'])
pal_xcel['(70,80)'].median()
stats_palb2=pal_xcel.describe()

palb_risk_v4['Age']=palb_risk_v4['Age'].astype('int64')
palb_risk_v4['age_range']=pd.cut(palb_risk_v4['Age'],bins=[20,30,40,50,60,70,80])
palb_risk_v4['BrCaRisk%']=palb_risk_v4['BrCaRisk%'].astype('float')
r = pd.pivot_table(palb_risk_v4,values='BrCaRisk%',columns=['Age'],index='IndivID')
r=r.T
r['Age']=r.index
r['age_range']=pd.cut(r['Age'],bins=[20,30,40,50,60,70,80])
y = pd.pivot_table(r,columns=['age_range'])
y=y.drop(index=['Age'])
palb2_stats=y.describe()

#for gene CHEK2
mer_chek2=pd.concat([chek_risk_v3,chek_risk_v4], axis=0)
mer_chek2=mer_chek2.drop(['OvCaRisk%', 'OvCaRisk%'], axis=1)

mer_chek2['Age']=mer_chek2['Age'].astype('int64')
mer_chek2['age_range']=pd.cut(mer_chek2['Age'],bins=[20,30,40,50,60,70,80])
mer_chek2['BrCaRisk%']=mer_chek2['BrCaRisk%'].astype('float')

mer_chek2['Version'] = mer_chek2['Version'].str.replace('v3','version3')
mer_chek2['Version'] = mer_chek2['Version'].str.replace('v4beta14','version4')

bx = sns.boxplot(x="age_range", y="BrCaRisk%", hue="Version",
                  data=mer_chek2,palette='colorblind', sym='').set_title('CHEK2')
plt.savefig('updated_CHEK2.png',dpi=500)

#descriptive statistics for version 3 (CHEK2)
chek_risk_v4['Age']=chek_risk_v4['Age'].astype('int64')
chek_risk_v4['age_range']=pd.cut(chek_risk_v4['Age'],bins=[20,30,40,50,60,70,80])
chek_risk_v3['BrCaRisk%']=chek_risk_v3['BrCaRisk%'].astype('float')
r = pd.pivot_table(chek_risk_v3,values='BrCaRisk%',columns=['age_range'],index='IndivID')
stats_chek2=r.describe()