import pandas as pd
import woSISconfig as cnf

# Class that has the pourpose of getting the Database from woSIS and merge them in one dataframe


class WoSISdb:
    def __init__(self):
        self.dataFrame = self.defineDataFrame()

    def defineDataFrame(self):
        #dfA = self.getAttributes()
        dfP = self.getProfiles()
        dfPh = self.getPhysical()
        dfC = self.getChemical()

        dfCharacteristics = pd.merge(
            dfPh, dfC, on=['profile_id', 'profile_layer_id'])
        df = pd.merge(dfP, dfCharacteristics)
        df.set_index(['profile_id', 'profile_layer_id'])
        return df

    def getAttributes(self):
        dfA = pd.read_csv('Code/DB/attributes.csv', sep='	', )
        dfA = dfA[cnf.attributes]
        return dfA

    def getProfiles(self):
        dfP = pd.read_csv('Code/DB/profiles.csv', sep='	',
                          dtype={'country_id': str})
        dfP = dfP[cnf.profiles]
        return dfP

    def getPhysical(self):
        dfPh = pd.read_csv('Code/DB/layers_physical.csv', sep='	')
        dfPh = dfPh[cnf.physichal]
        return dfPh

    def getChemical(self):
        dfC = pd.read_csv('Code/DB/layers_chemical.csv', sep='	')
        dfC = dfC[cnf.chemical]
        return dfC
