import pandas as pd
from sklearn import svm, preprocessing
from sklearn.cluster import KMeans
import numpy as np
from dbManager import DbManager
import datetime
from joblib import dump, load

from sklearn import metrics
from scipy.spatial.distance import cdist

import matplotlib.pyplot as plt


class Predictor:
    def __init__(self, typeP):
        self.dbManager = DbManager()
        self.type = typeP
        self.x = None
        self.y = None

    def predict(self, predictionData):
        if self.type == 'Kmeans':
            self.predictKmeans(predictionData)
        elif self.type == 'svm':
            pass

    def getGraphics(self):
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
        try:
            model = load('Kmeans.joblib')
        except:
            model = self.dumpKmeans()

        prediction = model.predict(predictionData)
        print(prediction)

    def dumpKmeans(self):
        self.x = self.dbManager.userDB
        self.x = self.x.drop(columns=['latitude', 'longitude'])
        self.x = preprocessing.normalize(self.x, norm='l2')
        model = KMeans(n_clusters=3, random_state=0)
        model.fit(self.x)
        dump(model, 'Kmeans.joblib')
        return model


s = [[0, 7.73,	0,	28.69,	0,	9.97,	0,	16.3,	0,	24.94,	0,
      23.06,	0,	9.04,	0,	19.37,	0,	-26.68,	0,	-21.31	, 0], [5, -9.66	, 0,	16.06	, 0,	23.16	, 0,	20.17	, 0,	19.35	, 0,	26.08	, 0,	3.58	, 0,	12.31	, 0,	19.13	, 0,	21.02	, 0
                                                            ]]
p = Predictor('Kmeans')
p.predict(s)
