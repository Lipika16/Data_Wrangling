
out_data_v4['Age']=out_data_v4['Age'].astype('int64')
out_data_v4['age_range']=pd.cut(out_data_v4['Age'],bins=[20,25,30,35,40,45,50,55,60,65,70,75,80])
out_data_v4['BrCaRisk%']=out_data_v4['BrCaRisk%'].astype('float')

a=out_data_v4[['BrCaRisk%','age_range','IndivID']]
b=a.groupby(['IndivID','age_range'],as_index=False)['BrCaRisk%'].mean()
c = pd.pivot_table(b,values='BrCaRisk%',columns=['age_range'], index=['IndivID'])
d=c.mean()
d=d.rename("version4")



out_data_v3['Age2']=out_data_v3['Age2'].astype('int64')
out_data_v3['age_bins']=pd.cut(out_data_v3['Age2'],bins=[20,25,30,35,40,45,50,55,60,65,70,75,80])
out_data_v3['BrCaRisk%2']=out_data_v3['BrCaRisk%2'].astype('float')

e=out_data_v3[['BrCaRisk%2','age_bins','IndivID2']]

f=e.groupby(['IndivID2','age_bins'],as_index=False)['BrCaRisk%2'].mean()
g = pd.pivot_table(f,values='BrCaRisk%2',columns=['age_bins'], index=['IndivID2'])
h=g.mean()
h=h.rename("version3")

mer=pd.concat([d, h], axis=1)
mer.plot.line()
mer.plot.box(sym='o')


axes = mer.plot.line(subplots=True)
type(axes)

lines = mer.plot.line(x='version4', y='version3')