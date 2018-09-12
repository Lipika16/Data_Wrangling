# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:12:10 2018

@author: Lipika Sharma
"""
import pandas as pd
org_data= pd.read_excel('../data/all_data.xlsx', usecols='E:AJ')

pedigrees=org_data['FamID'].value_counts()

#Histogram showing the number of individuals (unique) that a family has 

#classification based on age (have breast cancer/not have breast cancer)

#how many individuals are postives of each of the three genes

#a pdegiree structure

#male and female breast cancer

#breast and ovarian cancer comparison 



