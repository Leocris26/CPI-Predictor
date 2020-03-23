import pandas as pd
import woSISconfig as cnf


class WoSISdb:
    def __init__(self):
        self.dataFrame = self.defineDataFrame()

    def defineDataFrame(self):
        #dfA = self.getAttributes()
        dfP = self.getProfiles()
        dfPh = self.getPhysical()
        dfC = self.getChemical()

        df = pd.merge(dfP, dfPh, on='profile_id')
        df = pd.merge(df, dfC, on='profile_id')
        return df

    def getAttributes(self):
        dfA = pd.read_csv('./DB/attributes.csv', sep='	')
        dfA = dfA[cnf.attributes]
        return dfA

    def getProfiles(self):
        dfP = pd.read_csv('./DB/profiles.csv', sep='	')
        dfP = dfP[cnf.profiles]
        return dfP

    def getPhysical(self):
        dfPh = pd.read_csv('./DB/layers_physical.csv', sep='	')
        dfPh = dfPh[cnf.physichal]
        return dfPh

    def getChemical(self):
        dfC = pd.read_csv('./DB/layers_chemical.csv', sep='	')
        dfC = dfC[cnf.chemical]
        return dfC
