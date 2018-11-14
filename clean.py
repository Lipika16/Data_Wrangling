# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 00:04:34 2018

@author: Lipika Sharma
"""

#import pandas as pd
#import numpy as np
#org_data = pd.read_excel('Sharma_2018-07-24.xlsx', usecols='E:AJ')
#org_data= pd.read_excel('../data/sample.xlsx')

org_data=  pd.read_excel('../data/all_data.xlsx', usecols='E:AJ')
#org_data.set_index('Name', inplace=True)
 

#write a function 'pedigree check'
class Clean:
    
    def __init__(self,org_data):
        self.org_data = org_data
    
    def similar_IDs(self): 
        'PID and PID_MOTHER are the same.'
        self.org_data.loc[self.org_data['IndivID']==self.org_data['MothID'], 'MothID']=0
        'PID and PID_FATHER are the same.'
        self.org_data.loc[self.org_data['IndivID']==self.org_data['FathID'], 'FathID']=0
        'PIDs of parents are the same.'
        self.org_data.loc[self.org_data['FathID']==self.org_data['MothID'], 'MothID']=0
    
    def missing_parents(self):
        'PID_MOTHER is missing, both parent IDs must be given.'
        self.org_data.loc[self.org_data['MothID'] == 0, 'FathID'] = 0
        'PID_FATHER is missing, both parent IDs must be given.'
        self.org_data.loc[self.org_data['FathID'] == 0, 'MothID'] = 0
    
    def diff_parents_sex(self):
        'The mother of this person is not female.'
        self.org_data.loc[(self.org_data['Sex']=='M') & 
                     (self.org_data['IndivID'].isin(self.org_data['MothID'])),'Sex']='F'        
        'The father of this person is not male.'
        self.org_data.loc[(self.org_data['Sex']=='F') & 
                     (self.org_data['IndivID'].isin(self.org_data['FathID'])),'Sex']='M'
    
    def no_info_parents(self):
        'This person has a PID_MOTHER, but there is no row of data on her.'
        self.org_data.loc[~self.org_data['MothID'].isin(self.org_data['IndivID']), 'MothID']=0
        'This person has a PID_FATHER, but there is no row of data on him.'
        self.org_data.loc[~self.org_data['FathID'].isin(self.org_data['IndivID']), 'FathID']=0
    
    def min_members(self):
        'This family has only one member.'
        self.org_data=self.org_data.groupby("FamID").filter(lambda g: (g.FamID.size >= 3))
    
    def no_ID(self):
        'PID is missing'
        self.org_data=self.org_data.ix[~(self.org_data['IndivID'] == 0)]
    
    def twin_relation(self):
        'Twin relationship given, but not a twin ID.'
        self.org_data.loc[self.org_data['MZtwin']==1, ('IndivID', 'FamID')]
        twin=self.org_data['MZtwin']==1
        self.org_data.loc[twin & sum(twin) % 2 != 0 , 'MZtwin']=0
    
    def col_BC(self):
        'Contralateral BC indicated with no first BC indication.'
        self.org_data.loc[self.org_data['1stBrCa']==0, '2ndBrCa']=0 
        'Age of contralateral breast cancer is before age of first cancer'
        self.org_data.loc[self.org_data['2ndBrCa']<self.org_data['1stBrCa'], '2ndBrCa']=0
    
    def min_age_BC(self):
        'First breast cancer age indicated is before 10'
        self.org_data.loc[self.org_data['1stBrCa']<10, '1stBrCa']=0
        'Contralaterla breast cancer age indicated is before 10.'
        self.org_data.loc[self.org_data['2ndBrCa']<10, '2ndBrCa']=0
        'Ovarian cancer age indicated is before 10.'
        self.org_data.loc[self.org_data['OvCa']<10, 'OvCa']=0
    
    def clean_test_result(self):
        self.org_data.loc[self.org_data['BRCA1r']=='0', 'BRCA1t']=0
        self.org_data.loc[self.org_data['BRCA2r']=='0', 'BRCA2t']=0
        self.org_data.loc[self.org_data['PALB2r']=='0', 'PALB2t']=0
        self.org_data.loc[self.org_data['ATMr']=='0', 'ATMt']=0
        self.org_data.loc[self.org_data['CHEK2r']=='0', 'CHEK2t']=0
    
    def afterDeath_cancer(self):
        'First breast cancer age indicated is after death.'
        self.org_data.loc[(self.org_data['Dead']==1)&(self.org_data['1stBrCa']>self.org_data['Age']),
                     '1stBrCa']=0               
        'Contralateral breast age year is after death.'
        self.org_data.loc[(self.org_data['Dead']==1) & (self.org_data['2ndBrCa']>self.org_data['Age']), 
                     '2ndBrCa']=0
        'Ovarial cancer age indicated is after death.'
        self.org_data.loc[(self.org_data['Dead']==1) & (self.org_data['OvCa']>self.org_data['Age']),
                     'OvCa']=0
                         
#ped=org_data['FamID'].value_counts()
#org_data.fillna(0, inplace=True)
        
    def clean_data(self):
        self.similar_IDs()
        self.missing_parents()
        self.diff_parents_sex()
        self.no_info_parents()
        self.min_members()
        self.no_ID()
        self.twin_relation()
        self.col_BC()
        self.min_age_BC()
        self.clean_test_result()
        self.afterDeath_cancer()
