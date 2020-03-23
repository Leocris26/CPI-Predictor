import pandas as pd
import fieldMaintenanceActions as actions


class UserDB:
    def __init__(self):
        self.dataFrame = self.defineDataFrame()

    def defineDataFrame(self):
        dfU = self.getUserData()
        return dfU

    def getUserData(self):
        dfU = pd.read_csv('Code/UserData.csv', sep=',')
        for col in actions.actions:
            dfU[col] = pd.to_datetime(dfU[col])
            dfU[col] = dfU[col].mask(
                dfU[col].dt.year != 2019, dfU[col] + pd.offsets.DateOffset(year=2019))
            dfU[col] = dfU[col].apply(toTimeStamp)

        dfU.set_index('id')
        return dfU


def toTimeStamp(x):
    return x.timestamp()
