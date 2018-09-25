# -*- coding: utf-8 -*-
"""Created on Fri Aug  3 11:49:55 2018

@author: Lipika Sharma
"""
class Impute:
    
    def __init__(self,org_data):
        self.org_data = org_data
    
    def impute_age(self):
        check_year=int((self.org_data['Age']+self.org_data['Yob']).mode()[0])
        self.org_data.loc[self.org_data.Age.isnull(), 'Age']=check_year-self.org_data['Yob']

    def impute_dead(self):
        self.org_data.loc[(self.org_data.Dead.isnull()) &
                     (self.org_data['1stBrCa']!=0),'Dead']=1
             
        self.org_data.loc[(self.org_data.Dead.isnull()) & 
                          (self.org_data['Age']>85),'Dead']=1
             
        self.org_data['Dead'].fillna(0, inplace=True)

        self.org_data.loc[self.org_data['Age']>85, 'Age']=85

    def impute_Sex(self):
        self.org_data.loc[(self.org_data.Sex.isnull()) &
                     (self.org_data['IndivID'].isin(self.org_data['MothID'])),'Sex']='F'            
        self.org_data.loc[(self.org_data.Sex.isnull()) &
                     (self.org_data['IndivID'].isin(self.org_data['FathID'])),'Sex']='M'    
        
        self.org_data.loc[(self.org_data['Sex'].isnull()), 'Sex']='F'


    def impute_brca1(self):
        #brca1_miss=self.org_data[self.org_data['1stBrCa'].isnull()]
        self.org_data['1stBrCa'].fillna(0, inplace=True)

    def impute_brca2(self):
        #brca2_miss=self.org_data[self.org_data['2ndBrCa'].isnull()]
        self.org_data.loc[self.org_data['2ndBrCa'].isnull(), '2ndBrCa']=0

    def impute_OvCa(self):
        #ovca_miss=self.org_data[self.org_data['OvCa'].isnull()]
        self.org_data.loc[self.org_data['OvCa'].isnull(), 'OvCa']=0

    def impute_proca(self):
        #proca_miss=self.org_data[self.org_data['ProCa'].isnull()]
        self.org_data.loc[self.org_data['ProCa'].isnull(), 'ProCa']=0

    def impute_panca(self):
        #panca_miss=self.org_data[self.org_data['PanCa'].isnull()]
        self.org_data.loc[self.org_data['PanCa'].isnull(), 'PanCa']=0

    def impute_data(self):
        self.impute_age()
        self.impute_dead()
        self.impute_Sex()
        self.impute_brca1()
        self.impute_brca2()
        self.impute_OvCa()
        self.impute_proca()
        self.impute_panca()

        
        
        
'''org_data.fillna(0, inplace=True)
org_data.loc[(org_data['1stBrCa'].isnull())&
                     ((org_data['BRCA1r']=='P')|
                     (org_data['BRCA2r']=='P')|
                     (org_data['PALB2r']=='P')|
                     (org_data['ATMr']=='P')|
                     (org_data['CHEK2r']=='P')), '1stBrCa']=('AU').astype(int)'''
