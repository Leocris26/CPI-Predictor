import numpy as np
import pandas as pd
import woSISconfig as cnf

#dfA = pd.read_csv('attributes.csv', sep='	')
#dfP = pd.read_csv('profiles.csv', sep='	')
#dfPh = pd.read_csv('layers_physical.csv', sep='	')
#dfC = pd.read_csv('layers_chemical.csv', sep='	')

dfU = pd.read_csv('UserData.csv', sep=',')

#print(dfA.loc[:, ['code', 'description']])
#df = dfC[dfC[['nitkjd_value_avg']].notnull().all(axis=1)]
#df = df.loc[:, ['profile_id', 'profile_layer_id', 'nitkjd_value_avg']]
# print(df)
# with open("columnsProfiles.txt", "w") as text_file:
#    for col in dfP.columns:
#        print(col, file=text_file)
# print(dfC.columns)
#dfP = dfP[cnf.profiles]
#dfPh = dfPh[cnf.physichal]

#df = pd.merge(dfP, dfPh, on='profile_id')
dfU = dfU.infer_objects()
dfU['soil-sampling'] = pd.to_datetime(dfU['soil-sampling'])
print(dfU)
print(dfU.dtypes)
