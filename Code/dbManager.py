import pandas as pd
from woSIS import WoSISdb
from userDB import UserDB


class DbManager:
    def __init__(self):
        #self.woSISdf = self.getWoSIS()
        #self.woSISx = self.definewoSISx(self.woSISdf)
        #self.woSISy = self.definewoSISy(self.woSISdf)
        self.userDB = self.getUserData()

    def definewoSISx(self, df):
        dfX = df[['latitude', 'longitude']]
        return dfX

    def definewoSISy(self, df):
        dfY = df.drop(columns=['latitude', 'longitude'])
        return dfY

    def getWoSIS(self):
        wsDf = WoSISdb()
        return wsDf.dataFrame

    def getUserData(self):
        uDf = UserDB()
        return uDf.dataFrame
