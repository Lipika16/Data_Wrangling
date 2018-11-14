import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import epipy

all_data = pd.read_excel('data/cleaned_data.xlsx')

targets = all_data.loc[all_data['Target']==1, ('IndivID')]
tar_mom = all_data.loc[all_data['Target']==1, ('MothID')]
tar_fath = all_data.loc[all_data['Target']==1, ('FathID')]

mothers = all_data.loc[(all_data['Target']==1) & 
                         (all_data['IndivID'].isin(all_data['MothID'])), 'IndivID']

mothers = mothers.to_frame().reset_index()
mothers=mothers.rename({'IndivID':'MothID'}, axis='columns')

child=all_data[all_data['MothID'].isin(map(str,mothers['MothID']))]
all_child=child['IndivID']


sibling=all_data[all_data['MothID'].isin(map(str,list(tar_mom)))]
sibling = sibling.drop(sibling[sibling.MothID == 0].index)
all_sib=sibling['IndivID']


merge=pd.concat([targets,tar_mom,tar_fath, all_child,all_sib], axis=0)
merge=merge.rename("IndivID")

fir_deg_ped=all_data[all_data['IndivID'].isin(map(str,list(merge)))]

affec=fir_deg_ped.loc[fir_deg_ped['1stBrCa']!=0]

ped_mem=affec['FamID'].value_counts()
ped_mem = ped_mem.to_frame().reset_index()
ped_mem=ped_mem.rename({'index':'FamID','FamID':'Affected'}, axis='columns')
ped_mem=ped_mem.set_index('FamID')
ped_mem['FamID']=ped_mem.index
ped_mem=ped_mem['Affected'] - 1


out_data_v4=out_data_v4.set_index('FamID')
check = pd.merge(out_data_v4,ped_mem[['Affected']],on='FamID')

check['FamID']=check.index

palb_ind=all_data.loc[(all_data['PALB2r']=='P')&(all_data['Target']==1), 'IndivID']
chek_ind=all_data.loc[(all_data['CHEK2r']=='P')&(all_data['Target']==1),'IndivID']
atm_ind=all_data.loc[(all_data['ATMr']=='P')&(all_data['Target']==1),'IndivID']

palb_risk=check[check['IndivID'].isin(map(str,list(palb_ind)))]
chek_risk=check[check['IndivID'].isin(map(str,list(chek_ind)))]
atm_risk=check[check['IndivID'].isin(map(str,list(atm_ind)))]

palb_risk['Version'] = palb_risk['Version'].str.replace('v4beta14','PALB2')
chek_risk['Version'] = chek_risk['Version'].str.replace('v4beta14','CHEK2')
atm_risk['Version'] = atm_risk['Version'].str.replace('v4beta14','ATM')

mer=pd.concat([chek_risk,atm_risk,palb_risk], axis=0)

mer['Age']=mer['Age'].astype('int64')
mer['age_range']=pd.cut(mer['Age'],bins=[20,30,40,50,60,70,80])
mer['BrCaRisk%']=mer['BrCaRisk%'].astype('float')

mer=mer.rename({'Version':'Genes_version'}, axis='columns')


bx = sns.boxplot(x="Affected", y="BrCaRisk%", hue="Genes_version",
                  data=mer, palette='bright', sym='').set_title('First Degree Relatives')
plt.savefig('BOX_all.png',dpi=500)

