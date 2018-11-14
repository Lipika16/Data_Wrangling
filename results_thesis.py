# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:05:24 2018

@author: Lipika Sharma
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''Histogram showing the KDE distribution of the data 
    for number of individuals in a pedigree'''
all_data = pd.read_excel('data/cleaned_data.xlsx')
ped=all_data['FamID'].value_counts()
ped=ped.rename("Members")
frame=ped.to_frame(name=None)
frame.hist(column='Members')
plt.savefig('count_members',dpi=500)

sns.distplot(frame['Members']).set_title('Distribution of Number of Individuals in a Pegiree')
plt.savefig('pedigree_members',dpi=500)

stats=all_data.describe()
'''Histo for ages of targets'''
tar=all_data.loc[all_data['Target']==1,'Age']
tar_dat=tar.to_frame(name=None)
tar_dat.hist(column='Age')
plt.savefig('target_age',dpi=500)

sns.distplot(tar_dat['Age']).set_title('Distribution of Age of Targets')
plt.savefig('target_distri',dpi=500)

tar_dat['Age'].max()

all_affected=all_data.loc[all_data['1stBrCa']!=0,'IndivID']
all_non_aff=all_data.loc[all_data['1stBrCa']==0,'IndivID']

'''Stratified by gene'''
ind_palb=all_data.loc[(all_data['PALB2r']=='P')]
ind_chek=all_data.loc[(all_data['CHEK2r']=='P')]
ind_atm=all_data.loc[(all_data['ATMr']=='P')]

'ATM'
tar_atm=ind_atm.loc[ind_atm['Target']==1]
hea_atm=ind_atm.loc[(ind_atm['1stBrCa']==0)&(ind_atm['OvCa']==0)&
                    (ind_atm['ProCa']==0)&(ind_atm['PanCa']==0)]
uni_atm=ind_atm.loc[(ind_atm['1stBrCa']!=0)]
bi_atm=ind_atm.loc[(ind_atm['2ndBrCa']!=0)]
ova_atm=ind_atm.loc[(ind_atm['OvCa']!=0)]
ova_bc_atm=ind_atm.loc[(ind_atm['1stBrCa']!=0)&(ind_atm['OvCa']!=0)]

'CHEK2'
tar_chk=ind_chek.loc[ind_chek['Target']==1]
hea_chk=ind_chek.loc[(ind_chek['1stBrCa']==0)&(ind_chek['OvCa']==0)&
                    (ind_chek['ProCa']==0)&(ind_chek['PanCa']==0)]
uni_chk=ind_chek.loc[(ind_chek['1stBrCa']!=0)]
bi_chk=ind_chek.loc[(ind_chek['2ndBrCa']!=0)]
ova_chk=ind_chek.loc[(ind_chek['OvCa']!=0)]
ova_bc_chk=ind_chek.loc[(ind_chek['1stBrCa']!=0)&(ind_chek['OvCa']!=0)]

'PALB2'
tar_palb=ind_palb.loc[ind_palb['Target']==1]
hea_palb=ind_palb.loc[(ind_palb['1stBrCa']==0)&(ind_palb['OvCa']==0)&
                    (ind_palb['ProCa']==0)&(ind_palb['PanCa']==0)]
uni_palb=ind_palb.loc[(ind_palb['1stBrCa']!=0)]
bi_palb=ind_palb.loc[(ind_palb['2ndBrCa']!=0)]
ova_palb=ind_palb.loc[(ind_palb['OvCa']!=0)]
ova_bc_palb=ind_palb.loc[(ind_palb['1stBrCa']!=0)&(ind_palb['OvCa']!=0)]


#pie charts with the number of individuals positive for ATM, CHEK2, PALB2 
values = [ 243, 5, 180 , 56, 176, 25, 15]
values_chek = [1079, 14, 707, 339, 725, 110, 29]
values_palb = [307, 1, 209, 84, 203, 28, 18]
labels = ['Mutation-Positive Individuals', 'Breast Cancer and Ovarian Cancer','Index Cases', 
                         'Healthy Individual','Unilateral Breast Cancer',
                         'Bilateral Breast Cancer','Ovarian Cancer']
explode = (0.05, 0, 0, 0, 0, 0, 0)
plt.pie(values_chek, labels=None,
explode=explode, autopct='%1.1f%%',
counterclock=True)
plt.legend(labels,bbox_to_anchor=(1.0,0.8), loc="upper left")
plt.title('CHEK2')
plt.savefig('pie_CHEK2',dpi=500)

