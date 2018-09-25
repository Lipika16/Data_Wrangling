# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 00:45:30 2018

@author: Lipika Sharma
"""

import seaborn as sns
palb_risk['Age']=palb_risk['Age'].astype('int64')
palb_risk['BrCaRisk%']=palb_risk['BrCaRisk%'].astype('float')

a=palb_risk[['BrCaRisk%','Age','IndivID']]
b=a.groupby(['IndivID','Age'],as_index=False)['BrCaRisk%'].mean()

c = pd.pivot_table(b,values='BrCaRisk%',columns=['Age'], index=['IndivID'])
palb2=c.mean()
palb2=palb2.rename("PALB2")

#fig=c.plot.box(sym='o')


chek_risk['Age']=chek_risk['Age'].astype('int64')
chek_risk['BrCaRisk%']=chek_risk['BrCaRisk%'].astype('float')

x=chek_risk[['BrCaRisk%','Age','IndivID']]
y=x.groupby(['IndivID','Age'],as_index=False)['BrCaRisk%'].mean()

z = pd.pivot_table(y,values='BrCaRisk%',columns=['Age'], index=['IndivID'])
chek2=z.mean()
chek2=chek2.rename("CHKE2")


#fig=z.plot.box(sym='o')


atm_risk['Age']=atm_risk['Age'].astype('int64')
atm_risk['BrCaRisk%']=atm_risk['BrCaRisk%'].astype('float')

p=atm_risk[['BrCaRisk%','Age','IndivID']]
q=p.groupby(['IndivID','Age'],as_index=False)['BrCaRisk%'].mean()

r = pd.pivot_table(q,values='BrCaRisk%',columns=['Age'], index=['IndivID'])
atm=r.mean()
atm=atm.rename("ATM")




#fig=r.plot.box(sym='o')

#atm=243, chek=1079, palb=307 total_tar=1096

mer=pd.concat([palb2, chek2, atm], axis=1)
ax = sns.violinplot(x=)