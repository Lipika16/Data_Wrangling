import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mer['BrCaRisk%']=mer['BrCaRisk%'].astype('float')
mer['BrCaRisk%2']=mer['BrCaRisk%2'].astype('float')

mer['ratio'] = (mer['BrCaRisk%'] / mer['BrCaRisk%2'])

palb_risk=mer[mer['IndivID'].isin(map(str,list(palb_ind)))]
chek_risk=mer[mer['IndivID'].isin(map(str,list(chek_ind)))]
atm_risk=mer[mer['IndivID'].isin(map(str,list(atm_ind)))]

palb_risk['Version'] = palb_risk['Version'].str.replace('v4beta14','PALB2')
chek_risk['Version'] = chek_risk['Version'].str.replace('v4beta14','CHEK2')
atm_risk['Version'] = atm_risk['Version'].str.replace('v4beta14','ATM')

mer_ver=pd.concat([chek_risk,atm_risk,palb_risk], axis=0)

mer_ver['Age']=mer_ver['Age'].astype('int64')
mer_ver['age_range']=pd.cut(mer_ver['Age'],bins=[20,30,40,50,60,70,80])
mer_ver['BrCaRisk%']=mer_ver['BrCaRisk%'].astype('float')

mer_ver=mer_ver.rename({'Version':'Genes'}, axis='columns')


bx = sns.boxplot(x="age_range", y="ratio", hue="Genes",
                  data=mer_ver, palette='colorblind', sym='').set_title('Risk Ratio')
plt.savefig('risk_ratio.png',dpi=500)


out_data_v4['BrCaRisk%']=out_data_v4['BrCaRisk%'].astype('float')
out_data_v4['Age']=out_data_v4['Age'].astype('int64')
top_ext_v4=out_data_v4.loc[(out_data_v4['Age']==80)&
                        (out_data_v4['BrCaRisk%']>70), ('FamID', 'BrCaRisk%')]

bottom_ext=out_data_v4.loc[(out_data_v4['Age']==80)&
                        (out_data_v4['BrCaRisk%']<2.8), ('FamID', 'BrCaRisk%')]
