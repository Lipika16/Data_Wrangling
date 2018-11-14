# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:14:23 2018

@author: Lipika Sharma
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

all_data = pd.read_excel('../data/cleaned_data.xlsx')
non_affec=all_data.loc[(all_data['Target']==1)&(all_data['1stBrCa']==0)]

palb_ind=non_affec.loc[(non_affec['PALB2r']=='P')&(non_affec['Target']==1), 'IndivID']
chek_ind=non_affec.loc[(non_affec['CHEK2r']=='P')&(non_affec['Target']==1),'IndivID']
atm_ind=non_affec.loc[(non_affec['ATMr']=='P')&(non_affec['Target']==1),'IndivID']


palb_risk=out_data_v4[out_data_v4['IndivID'].isin(map(str,list(palb_ind)))]
chek_risk=out_data_v4[out_data_v4['IndivID'].isin(map(str,list(chek_ind)))]
atm_risk=out_data_v4[out_data_v4['IndivID'].isin(map(str,list(atm_ind)))]

v3=out_data_v3[out_data_v3['IndivID'].isin(map(str,out_data_v4['IndivID']))]

palb_risk_v3=v3[v3['IndivID'].isin(map(str,list(palb_ind)))]
chek_risk_v3=v3[v3['IndivID'].isin(map(str,list(chek_ind)))]
atm_risk_v3=v3[v3['IndivID'].isin(map(str,list(atm_ind)))]

atm_risk['BrCaRisk%']=atm_risk['BrCaRisk%'].astype('float')
atm_risk['BrCaRisk%'].describe()

#for PALB
mer_atm=pd.concat([atm_risk_v3,atm_risk], axis=0)
mer_atm['Version'] = mer_atm['Version'].str.replace('v3','version3')
mer_atm['Version'] = mer_atm['Version'].str.replace('v4beta14','version4')

mer_atm['Age']=mer_atm['Age'].astype('int64')
mer_atm['age_range']=pd.cut(mer_atm['Age'],bins=[20,30,40,50,60,70,80])
mer_atm['BrCaRisk%']=mer_atm['BrCaRisk%'].astype('float')

bx = sns.boxplot(x="age_range", y="BrCaRisk%", hue="Version",
                  data=mer_atm, palette='husl', sym='').set_title('Non-Affected ATM Individuals')
plt.savefig('non.aff_atm.png',dpi=500)
mer_atm['BrCaRisk%'].describe()

