# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 13:25:55 2018

@author: Lipika Sharma
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#import epipy

all_data = pd.read_excel('../data/cleaned_data.xlsx')

data_all=[]
with open('../data/all_genes_risk.txt','r') as f:
    next(f)
    for line in f:
        data_all.append(line.split())
columns_all=['FamID','SessionNum','CalNum','Name','IndivID','Version',
         'Age','BrCaRisk','BrCaRisk%','OvCaRisk','OvCaRisk%']
data_all=pd.DataFrame(data_all,columns=columns_all)
data_all=data_all[columns_all]

all_data_v4=data_all[['FamID','IndivID','Version','Age','BrCaRisk%','OvCaRisk%']]


palb_ind=all_data.loc[(all_data['PALB2r']=='P')&(all_data['Target']==1),'IndivID']
chek_ind=all_data.loc[(all_data['CHEK2r']=='P')&(all_data['Target']==1),'IndivID']
atm_ind=all_data.loc[(all_data['ATMr']=='P')&(all_data['Target']==1),'IndivID']

palb_risk=all_data_v4[all_data_v4['IndivID'].isin(map(str,list(palb_ind)))]
chek_risk=all_data_v4[all_data_v4['IndivID'].isin(map(str,list(chek_ind)))]
atm_risk=all_data_v4[all_data_v4['IndivID'].isin(map(str,list(atm_ind)))]



#version 3
data_v3=[]
with open('../data/all_genes_version3.txt','r') as f:
    next(f)
    for line in f:
        data_v3.append(line.split())
columns_v3=['FamID','Date','Time','SessionNum','CalNum','Name','IndivID','Version',
         'Age','BrCaRisk','BrCaRisk%','OvCaRisk','OvCaRisk%']
data_v3=pd.DataFrame(data_v3,columns=columns_v3)
data_v3=data_v3[columns_v3]
out_data_v3=data_v3[['FamID','IndivID','Version','Age','BrCaRisk%','OvCaRisk%']]


v3=out_data_v3[out_data_v3['IndivID'].isin(map(str,list(atm_ind)))]
mer=pd.concat([v3,atm_risk], axis=0)
mer=mer.drop(['OvCaRisk%', 'OvCaRisk%'], axis=1)

mer['Age']=mer['Age'].astype('int64')
mer['age_range']=pd.cut(mer['Age'],bins=[20,30,40,50,60,70,80])
mer['BrCaRisk%']=mer['BrCaRisk%'].astype('float')

mer['Version'] = mer['Version'].str.replace('v3','version3')
mer['Version'] = mer['Version'].str.replace('v4beta14','version4')

bx = sns.boxplot(x="age_range", y="BrCaRisk%", hue="Version",
                  data=mer,palette='colorblind', sym='').set_title('ATM')
plt.savefig('unaff_atm.png',dpi=500)

palb_risk['Age']=palb_risk['Age'].astype('int64')
palb_risk['age_range']=pd.cut(palb_risk['Age'],bins=[20,30,40,50,60,70,80])
palb_risk['BrCaRisk%']=palb_risk['BrCaRisk%'].astype('float')
r = pd.pivot_table(palb_risk,values='BrCaRisk%',columns=['age_range'],index='IndivID')
a=r.describe()

v3['Age']=v3['Age'].astype('int64')
v3['age_range']=pd.cut(v3['Age'],bins=[20,30,40,50,60,70,80])
v3['BrCaRisk%']=v3['BrCaRisk%'].astype('float')
s = pd.pivot_table(v3,values='BrCaRisk%',columns=['age_range'],index='IndivID')
b=s.describe()


#extreme families
palb_risk['Version'] = palb_risk['Version'].str.replace('v4beta14','PALB2')
chek_risk['Version'] = chek_risk['Version'].str.replace('v4beta14','CHEK2')
atm_risk['Version'] = atm_risk['Version'].str.replace('v4beta14','ATM')

palb_risk['BrCaRisk%']=palb_risk['BrCaRisk%'].astype('float')
palb_risk['Age']=palb_risk['Age'].astype('int64')
top_ext_palb=palb_risk.loc[(palb_risk['Age']==80)&
                        (palb_risk['BrCaRisk%']>38), ('FamID', 'BrCaRisk%')]

bottom_ext_palb=palb_risk.loc[(palb_risk['Age']==80)&
                        (palb_risk['BrCaRisk%']<29.5), ('FamID', 'BrCaRisk%')]

chek_risk['BrCaRisk%']=chek_risk['BrCaRisk%'].astype('float')
chek_risk['Age']=chek_risk['Age'].astype('int64')
top_ext_chek=chek_risk.loc[(chek_risk['Age']==80)&
                        (chek_risk['BrCaRisk%']>45), ('FamID', 'BrCaRisk%')]

bottom_ext_chek=chek_risk.loc[(chek_risk['Age']==80)&
                        (chek_risk['BrCaRisk%']<24), ('FamID', 'BrCaRisk%')]

atm_risk['BrCaRisk%']=atm_risk['BrCaRisk%'].astype('float')
atm_risk['Age']=atm_risk['Age'].astype('int64')
top_ext_atm=atm_risk.loc[(atm_risk['Age']==80)&
                        (atm_risk['BrCaRisk%']>30), ('FamID', 'BrCaRisk%')]

bottom_ext_atm=atm_risk.loc[(atm_risk['Age']==80)&
                        (atm_risk['BrCaRisk%']<29.9), ('FamID', 'BrCaRisk%')]


#for gettting all the unaffected individuals
all_genes=all_data.loc[(all_data['Target']==1)&(all_data['1stBrCa']==0), 'FamID']
all_ped=all_data[all_data['FamID'].isin(map(str,list(all_genes)))]

all_pos=all_ped.loc[(all_ped['Target']==1)&((all_ped['PALB2r']=='P')|
(all_ped['CHEK2r']=='P')|(all_ped['ATMr']=='P')),'FamID']

affec_all=all_data[all_data['FamID'].isin(map(str,list(all_pos)))]

#version 4
with open('data/all_genes.txt','w') as f:
    header='BOADICEA import pedigree file format 4.0\n'
    f.write(header)
    affec_all.to_csv(f,index=False,sep='\t', float_format=np.int64)

#version 3
v3_data=affec_all
v3_data=v3_data.drop(columns=['BRCA1t','BRCA1r', 'BRCA2t', 'BRCA2r', 'PALB2t', 
                                'PALB2r', 'ATMt','ATMr',
                                'CHEK2t','CHEK2r' ])
v3_data=v3_data.rename({'MZtwin':'Twin','1stBrCa':'1BrCa', '2ndBrCa':'2BrCa', 
                              }, axis='columns')

v3_data.insert(loc=16, column='Gtest', value=0)
v3_data.insert(loc=17, column='Mutn', value=0)

with open('data/all_genes_version3.txt','w') as f:
    header='BOADICEA import pedigree file format 2.0\n'
    f.write(header)
    v3_data.to_csv(f,index=False,sep='\t', float_format=np.int64)
