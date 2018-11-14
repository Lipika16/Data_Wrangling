# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:12:10 2018

@author: Lipika Sharma

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#import epipy

all_data = pd.read_excel('data/cleaned_data.xlsx')
tar=all_data.loc[all_data['Target']==1]

palb_ind=all_data.loc[(all_data['PALB2r']=='P')&(all_data['Target']==1), 'IndivID']
chek_ind=all_data.loc[(all_data['CHEK2r']=='P')&(all_data['Target']==1),'IndivID']
atm_ind=all_data.loc[(all_data['ATMr']=='P')&(all_data['Target']==1),'IndivID']

palb_risk=out_data_v4[out_data_v4['IndivID'].isin(map(str,list(palb_ind)))]
palb_risk['Version'] = palb_risk['Version'].str.replace('v4beta14','Version4')

chek_risk=out_data_v4[out_data_v4['IndivID'].isin(map(str,list(chek_ind)))]
atm_risk=out_data_v4[out_data_v4['IndivID'].isin(map(str,list(atm_ind)))]

palb_risk_v3=v3[v3['IndivID'].isin(map(str,list(palb_ind)))]
palb_risk_v3['Version'] = palb_risk_v3['Version'].str.replace('v3','Version3')

chek_risk_v3=v3[v3['IndivID'].isin(map(str,list(chek_ind)))]
atm_risk_v3=v3[v3['IndivID'].isin(map(str,list(atm_ind)))]

mer_atm = pd.concat([atm_risk_v3, atm_risk], axis=0)
mer_palb = pd.concat([palb_risk_v3, palb_risk], axis=0)
mer_chek = pd.concat([palb_risk_v3, palb_risk], axis=0)

bx = sns.boxplot(x="age_range", y="BrCaRisk%", hue="Version",
                  data=mer_palb,palette='colorblind', sym='').set_title('Breast Cancer Risks for PALB2 Mutation Carriers')
plt.savefig('thesis_palb2carriers',dpi=500)

palb_risk['Version'] = palb_risk['Version'].str.replace('v4beta14','PALB2')
chek_risk['Version'] = chek_risk['Version'].str.replace('v4beta14','CHEK2')
atm_risk['Version'] = atm_risk['Version'].str.replace('v4beta14','ATM')









mer=pd.concat([v3,chek_risk,atm_risk,palb_risk], axis=0)

mer['Age']=mer['Age'].astype('int64')
mer['age_range']=pd.cut(mer['Age'],bins=[20,30,40,50,60,70,80])
mer['BrCaRisk%']=mer['BrCaRisk%'].astype('float')

mer=mer.rename({'Version':'Genes_version'}, axis='columns')


bx = sns.boxplot(x="age_range", y="BrCaRisk%", hue="Genes_version",
                  data=mer, palette='Set2', sym='')
plt.savefig('BOX_all.png',dpi=500)


g = sns.lmplot(x="Age", y="BrCaRisk%", col="Genes", hue="Genes",
                data=mer, height=6, aspect=.4, x_jitter=.1)

ax = sns.scatterplot(x=("Age"), y="BrCaRisk%", hue="Genes",
                  data=mer, palette="muted")

sns.relplot(x="Age", y="BrCaRisk%", hue="Status", size="Status",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=mer)
plt.savefig('scatterplot.png',dpi=500)
plt.close()

sns.catplot(x="Age", y="BrCaRisk%", hue="Genes", kind="swarm", data=mer);




r = pd.pivot_table(mer,values='BrCaRisk%',columns=['Genes'], index=['age_range'])
r.plot.hist(stacked=True, bins=20)
plt.savefig('freq1.png',dpi=500)
plt.close()

df = df.cumsum()

plt.savefig('boxplot_genes.png',dpi=500)
plt.close()



palb_risk['Age']=palb_risk['Age'].astype('int64')
palb_risk['age_range']=pd.cut(palb_risk['Age'],bins=[20,30,40,50,60,70,80])
palb_risk['BrCaRisk%']=palb_risk['BrCaRisk%'].astype('float')

a=palb_risk[['BrCaRisk%','age_range','IndivID']]
b=a.groupby(['IndivID','age_range'],as_index=False)['BrCaRisk%'].mean()

c = pd.pivot_table(b,values='BrCaRisk%',columns=['age_range'], index=['IndivID'])
palb2=c.mean()
palb2=palb2.rename("PALB2")

#fig=c.plot.box(sym='o')


chek_risk['Age']=chek_risk['Age'].astype('int64')
chek_risk['age_range']=pd.cut(chek_risk['Age'],bins=[20,30,40,50,60,70,80])
chek_risk['BrCaRisk%']=chek_risk['BrCaRisk%'].astype('float')

a=chek_risk[['BrCaRisk%','age_range','IndivID']]
b=a.groupby(['IndivID','age_range'],as_index=False)['BrCaRisk%'].mean()

c = pd.pivot_table(b,values='BrCaRisk%',columns=['age_range'], index=['IndivID'])
chek2=c.mean()
chek2=chek2.rename("CHEK2")


#fig=z.plot.box(sym='o')


atm_risk['Age']=atm_risk['Age'].astype('int64')
atm_risk['age_range']=pd.cut(atm_risk['Age'],bins=[20,30,40,50,60,70,80])
atm_risk['BrCaRisk%']=atm_risk['BrCaRisk%'].astype('float')

p=atm_risk[['BrCaRisk%','age_range','IndivID']]
q=p.groupby(['IndivID','age_range'],as_index=False)['BrCaRisk%'].mean()

r = pd.pivot_table(q,values='BrCaRisk%',columns=['age_range'], index=['IndivID'])
atm=r.mean()
atm=atm.rename("ATM")


df = pd.DataFrame({
    'PALB2': [0.583333, 3.62645, 12.3552, 23.2689, 35.7475, 44.375],
    'CHEK2': [0.12, 1.34755, 5.35842, 12.913, 23.5432, 31.5243],
    'ATM' :  [0.21875, 1.48471, 6.65091, 15.2957, 24.8265, 32.0754]
    }, index=[30, 40, 50, 60, 70, 80])
lines = df.plot.line()
plt.savefig('line.png',dpi=500)
plt.close()

#fig=r.plot.box(sym='o')

#atm=243, chek=1079, palb=307 total_tar=1096

mer=pd.concat([palb2, chek2, atm], axis=1)

as_list = mer.index.tolist()
idx = as_list.index('(20,30]')
as_list[idx] = 'South Korea'
df.index = as_list

mer.plot.line()
mer.plot.box(sym='o')

ax = sns.boxplot(mer)

axes = mer.plot.scatter(subplots=True)
type(axes)


affec=all_data.loc[(all_data['Target']==1)&(all_data['1stBrCa']!=0), 'IndivID']
non_affec=all_data.loc[(all_data['Target']==1)&(all_data['1stBrCa']==0), 'IndivID']


aff=out_data_v4[out_data_v4['IndivID'].isin(map(str,list(affec)))]
non=out_data_v4[out_data_v4['IndivID'].isin(map(str,list(non_affec)))]


palb_ind=all_data.loc[(all_data['PALB2r']=='P')&(all_data['Target']==1), 'IndivID']
chek_ind=all_data.loc[(all_data['CHEK2r']=='P')&(all_data['Target']==1),'IndivID']
atm_ind=all_data.loc[(all_data['ATMr']=='P')&(all_data['Target']==1),'IndivID']

palb_risk=non[non['IndivID'].isin(map(str,list(palb_ind)))]
chek_risk=non[non['IndivID'].isin(map(str,list(chek_ind)))]
atm_risk=non[non['IndivID'].isin(map(str,list(atm_ind)))]

palb_risk['Version'] = palb_risk['Version'].str.replace('v4beta14','PALB2')
chek_risk['Version'] = chek_risk['Version'].str.replace('v4beta14','CHEK2')
atm_risk['Version'] = atm_risk['Version'].str.replace('v4beta14','ATM')

mer=pd.concat([chek_risk,atm_risk,palb_risk], axis=0)

mer['Age']=mer['Age'].astype('int64')
mer['age_range']=pd.cut(mer['Age'],bins=[20,30,40,50,60,70,80])
mer['BrCaRisk%']=mer['BrCaRisk%'].astype('float')

mer=mer.rename({'Version':'Genes_version'}, axis='columns')


bx = sns.boxplot(x="age_range", y="BrCaRisk%", hue="Genes_version",
                  data=mer, palette='bright', sym='').set_title('Risks for non-affected individuals ')
plt.savefig('affec.png',dpi=500)




aff['Version'] = aff['Version'].str.replace('v4beta14','Affected')
non['Version'] = non['Version'].str.replace('v4beta14','Non-Affected')

mer=pd.concat([aff,non], axis=0)

mer['Age']=mer['Age'].astype('int64')
mer['age_range']=pd.cut(mer['Age'],bins=[20,30,40,50,60,70,80])
mer['BrCaRisk%']=mer['BrCaRisk%'].astype('float')

mer=mer.rename({'Version':'Status'}, axis='columns')

bx = sns.boxplot(x="age_range", y="BrCaRisk%", hue="Status",
                  data=mer, palette="muted", sym='')
plt.savefig('status.png',dpi=500)

male=all_data.loc[(all_data['Target']==1)&(all_data['Sex']=='M'), 'IndivID']
female=all_data.loc[(all_data['Target']==1)&(all_data['Sex']=='F'), 'IndivID']





#Histogram showing the number of individuals (unique) that a family has 

#classification based on age (have breast cancer/not have breast cancer)

#how many individuals are postives of each of the three genes

#a pdegiree structure

#male and female breast cancer

#breast and ovarian cancer comparison 