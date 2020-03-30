import pandas as pd
import fieldMaintenanceActions as actions

# Class that has the pourpose of getting the userData


class UserDB:
    def __init__(self):
        self.dataFrame = self.defineDataFrame()

    def defineDataFrame(self):
        dfU = self.getUserData()
        return dfU

    def getUserData(self):
        dfU = pd.read_csv('Code/UserData.csv', sep=',')
        # The for cycle transform the data to a timestamp, they are all first transformed to a
        # 2019 date, and then getting their thimestamps, so they are in the same range of values

        for col in actions.actions:
            dfU[col] = pd.to_datetime(dfU[col])
            dfU[col] = dfU[col].mask(
                dfU[col].dt.year != 2019, dfU[col] + pd.offsets.DateOffset(year=2019))
            dfU[col] = dfU[col].apply(toTimeStamp)

        dfU.set_index('id')
        return dfU


def toTimeStamp(x):
    return x.timestamp()
