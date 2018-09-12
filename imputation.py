# -*- coding: utf-8 -*-
"""Created on Fri Aug  3 11:49:55 2018

@author: Lipika Sharma
"""
org_data.isnull().sum()
check_year=int((org_data['Age']+org_data['Yob']).mode()[0])

'FEW ASSUMPTIONS'
'1 IMPUTING AGE'
org_data.loc[org_data.Age.isnull(), 'Age']=check_year-org_data['Yob']


'2 IMPUTING DEAD'
org_data.loc[(org_data.Dead.isnull()) &
             (org_data['1stBrCa']!=0),'Dead']=1
             
org_data.loc[(org_data.Dead.isnull()) & (org_data['Age']>85),
             'Dead']=1
             
org_data['Dead'].fillna(0, inplace=True)


org_data.loc[org_data['Age']>85, 'Age']=85


'3 IMPUTING SEX'
org_data.loc[(org_data.Sex.isnull()) &
             (org_data['IndivID'].isin(org_data['MothID'])),'Sex']='F'

            
org_data.loc[(org_data.Sex.isnull()) &
             (org_data['IndivID'].isin(org_data['FathID'])),'Sex']='M'    

org_data.loc[(org_data['Sex'].isnull()), 'Sex']='F'


'4 IMPUTING 1STBRCA'
brca1_miss=org_data[org_data['1stBrCa'].isnull()]
'''
org_data.loc[(org_data['1stBrCa'].isnull())&
             ((org_data['BRCA1r']=='P')|
             (org_data['BRCA2r']=='P')|
             (org_data['PALB2r']=='P')|
             (org_data['ATMr']=='P')|
             (org_data['CHEK2r']=='P')), '1stBrCa']=('AU').astype(int)
'''
org_data['1stBrCa'].fillna(0, inplace=True)

'5 IMPUTING 2NDBRCA'
brca2_miss=org_data[org_data['2ndBrCa'].isnull()]
org_data.loc[org_data['2ndBrCa'].isnull(), '2ndBrCa']=0

'6 IMPUTING OVCA'
ovca_miss=org_data[org_data['OvCa'].isnull()]
org_data.loc[org_data['OvCa'].isnull(), 'OvCa']=0

'7 IMPUTING PROCA'
proca_miss=org_data[org_data['ProCa'].isnull()]
org_data.loc[org_data['ProCa'].isnull(), 'ProCa']=0

'8 IMPUTING PANCA'
panca_miss=org_data[org_data['PanCa'].isnull()]
org_data.loc[org_data['PanCa'].isnull(), 'PanCa']=0


#org_data.fillna(0, inplace=True)

