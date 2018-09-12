# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 12:45:57 2018

@author: Lipika Sharma
"""

import pandas as pd
import numpy as np
v3_data=org_data
v3_data=v3_data.drop(columns=['BRCA1t','BRCA1r', 'BRCA2t', 'BRCA2r', 'PALB2t', 
                                'PALB2r', 'ATMt','ATMr',
                                'CHEK2t','CHEK2r' ])
v3_data=v3_data.rename({'MZtwin':'Twin','1stBrCa':'1BrCa', '2ndBrCa':'2BrCa', 
                              }, axis='columns')

v3_data.insert(loc=16, column='Gtest', value=0)
v3_data.insert(loc=17, column='Mutn', value=0)

ped=v3_data['FamID'].unique()
fam_len=int((len(ped) - len(ped)%3)/3)
#ped = pd.Series(ped)
v3_data.dtypes
for i in range(3):
    part = v3_data[v3_data['FamID'].isin(ped[fam_len*i:fam_len*(i+1)])]
    with open('../data/version3_out'+str(i+1)+'.txt','w') as f:
        header='BOADICEA import pedigree file format 2.0\n'
        f.write(header)
        part.to_csv(f,index=False,sep='\t', float_format=np.int64)
