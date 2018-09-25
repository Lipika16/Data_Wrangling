import pandas as pd
#import numpy as np

#org_data = pd.read_excel('Sharma_2018-07-24.xlsx', usecols='E:AJ')
#org_data= pd.read_excel('../data/all_data.xlsx', usecols='E:AJ')
#backup_data=org_data

from clean import Clean
clean = Clean(org_data)
clean.clean_data()
org_data = clean.org_data

from imputation import Impute
impute=Impute(org_data)
impute.impute_data()
org_data = impute.org_data