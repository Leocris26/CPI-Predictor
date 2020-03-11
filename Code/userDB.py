import pandas as pd
import fieldMaintenanceActions as actions


class UserDB:
    def __init__(self):
        self.dataFrame = self.defineDataFrame()

    def defineDataFrame(self):
        dfU = self.getUserData()
        print(dfU.dtypes)
        return dfU

    def getUserData(self):
        dfU = pd.read_csv('UserData.csv', sep=',')
        dfU.set_index('id')
        for col in actions.actions:
            dfU[col] = pd.to_datetime(dfU[col])
            dfU[col] = dfU[col].mask(
                dfU[col].dt.year != 2019, dfU[col] + pd.offsets.DateOffset(year=2019))
            dfU[col] = dfU[col].apply(toTimeStamp)

        return dfU


def toTimeStamp(x):
    return x.timestamp()
