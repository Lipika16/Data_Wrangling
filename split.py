import pandas as pd
import numpy as np
#org_all = pd.read_excel('../data/all_data.xlsx', usecols='E:AJ')
#org_all.fillna(0, inplace=True)
#org_all[['Name','FamID']].groupby('FamID').agg('count')
ped=org_data['FamID'].unique()
fam_len=int((len(ped) - len(ped)%100)/100)
#ped = pd.Series(ped)
org_data.dtypes

for i in range(100):
    part = org_data[org_data['FamID'].isin(ped[fam_len*i:fam_len*(i+1)])]
    print(i,len(part))
    with open('../data/version4_out'+str(i+1)+'.txt','w') as f:
        header='BOADICEA import pedigree file format 4.0\n'
        f.write(header)
        part.to_csv(f,index=False,sep='\t', float_format=np.int64)