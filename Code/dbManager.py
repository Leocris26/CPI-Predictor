import pandas as pd
from woSIS import WoSISdb
from userDB import UserDB



class DbManager:
    def __init__(self, type):
        self.woSISx = None
        self.woSISy = None
        self.userDB = None
        if (type == 0):
            self.getWoSIS()
        else:
            self.userDB = self.getUserData()

    def definewoSISx(self, df):
        dfX = df[['latitude', 'longitude']]
        self.woSISx = dfX

    def definewoSISy(self, df):
        dfY = df.drop(columns=['latitude', 'longitude'])
        dfY.set_index('profile_id')
        dfY.set_index('profile_layer_id')
        self.woSISy = dfY

    def getWoSIS(self):
        # Here is where the dataframe is limited to only US territory and then that column is dropped
        # Also the dataframe is divided into X and y.
        wsDf = WoSISdb()
        wsDf.dataFrame = wsDf.dataFrame.loc[wsDf.dataFrame['country_id'] == 'US']
        wsDf.dataFrame = wsDf.dataFrame.drop(columns=['country_id'])
        self.definewoSISx(wsDf.dataFrame)
        self.definewoSISy(wsDf.dataFrame)

    def getUserData(self):
        uDf = UserDB()
        return uDf.dataFrame
