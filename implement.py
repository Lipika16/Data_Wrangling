import pandas as pd
org_data= pd.read_excel('../data/all_data.xlsx', usecols='E:AJ')
org_data.loc[org_data['BRCA1r']==0, 'BRCA1t']=0
org_data.loc[org_data['BRCA2r']==0, 'BRCA2t']=0
org_data.loc[org_data['PALB2r']==0, 'PALB2t']=0
org_data.loc[org_data['ATMr']==0, 'ATMt']=0
org_data.loc[org_data['CHEK2r']==0, 'CHEK2t']=0


