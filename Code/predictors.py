import pandas as pd
from sklearn import svm, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.svm import SVR
import numpy as np
from dbManager import DbManager
import datetime
from joblib import dump, load
from sklearn.multioutput import MultiOutputRegressor

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

from sklearn import metrics
from scipy.spatial.distance import cdist

import matplotlib.pyplot as plt


class Predictor:
    def __init__(self, typeP):
        self.type = typeP
        self.x = None
        self.y = None

    def predict(self, predictionData):
        if self.type == 'Kmeans':
            self.predictKmeans(predictionData)
        elif self.type == 'SVM':
            self.predictSVM(predictionData)

    def getKmeansGraphics(self):

        # It plot both graphics for elbow method
        distortions = []
        inertias = []
        mapping1 = {}
        mapping2 = {}
        K = range(1, 10)

        for k in K:
            # Building and fitting the model
            kmeanModel = KMeans(n_clusters=k).fit(self.x)
            kmeanModel.fit(self.x)

            distortions.append(sum(np.min(cdist(self.x, kmeanModel.cluster_centers_,
                                                'euclidean'), axis=1)) / self.x.shape[0])
            inertias.append(kmeanModel.inertia_)

            mapping1[k] = sum(np.min(cdist(self.x, kmeanModel.cluster_centers_,
                                           'euclidean'), axis=1)) / self.x.shape[0]
            mapping2[k] = kmeanModel.inertia_

        for key, val in mapping1.items():
            print(str(key)+' : '+str(val))

        plt.plot(K, distortions, 'bx-')
        plt.xlabel('Cantidad de grupos')
        plt.ylabel('Distorsión')
        plt.title('El método del codo usando Distorsión')
        plt.show()

        plt.plot(K, inertias, 'bx-')
        plt.xlabel('Cantidad de grupos')
        plt.ylabel('Inercia')
        plt.title('El método del codo usando Inercia')
        plt.show()

    def predictKmeans(self, predictionData):

        # If it finds the joblib , it would use it for predicting, if not, it will create the joblib
        try:
            model = load('Code/joblibs/Kmeans.joblib')
        except:
            model = self.dumpKmeans()

        prediction = model.predict(predictionData)
        print(prediction)

    def predictSVM(self, predictionData):
        try:
            model = load('Code/joblibs/SVM.joblib')
        except:
            model = self.dumpSVM()
        prediction = model.predict(predictionData)
        print(prediction)

    def dumpKmeans(self):
        # Process of dumping kmeans
        # Train and test models needed to be implemented ******
        self.dbManager = DbManager(1)
        self.x = self.dbManager.userDB
        self.x = self.x.drop(columns=['latitude', 'longitude'])
        self.x = preprocessing.normalize(self.x, norm='l2')
        model = KMeans(n_clusters=3, random_state=0)
        model.fit(self.x)
        dump(model, 'Code/joblibs/Kmeans.joblib')
        return model

    def dumpSVM(self):
        self.dbManager = DbManager(0)
        self.x = self.dbManager.woSISx
        self.y = self.dbManager.woSISy
        # Getting rid off of the NaN values, but, since i'm getting from the dirt, i think that converting NaN values to 0 would work as well, more research needed

        estimator = IterativeImputer(random_state=0)
        yFilled = estimator.fit_transform(self.y)
        #
        X = self.x
        y = yFilled

        X = preprocessing.scale(X)

        X = np.array(X)
        y = np.array(y)

        # Debugging 101
        print('So far so good 1')
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.4)
        print('So far so good 2')

        # MultiOutputRegressor is my first try to make a prediction that can use a matrix output, but it's not working
        # n-job = -1 is for using all processors avaiable,
        # i'll be reading about other models
        model = MultiOutputRegressor(estimator=SVR(), n_jobs=-1)
        print('So far so good 3')

        # Here's where the code gets stuck, and kinda froze everything, the fit of the model
        # at this point trying to cancel the execution with ctrl + c doesn't respond
        model.fit(X_train, y_train)
        print('So far so good 4')

        confidence = model.score(X_test, y_test)
        print('So far so good 5')

        print(confidence)
        dump(model, 'Code/joblibs/SVM.joblib')
        return model


# Input for Kmeans, but i'm not sure about this input, it is accpeted in shape but the values should be other i think
s = [[0, 7.73,	0,	28.69,	0,	9.97,	0,	16.3,	0,	24.94,	0,
      23.06,	0,	9.04,	0,	19.37,	0,	-26.68,	0,	-21.31	, 0], [5, -9.66	, 0,	16.06	, 0,	23.16	, 0,	20.17	, 0,	19.35	, 0,	26.08	, 0,	3.58	, 0,	12.31	, 0,	19.13	, 0,	21.02	, 0
                                                            ]]

# Input for SVM
z = [[38.290600, -100.232769]]
p = Predictor('Kmeans')
p.predict(s)
