import pandas as pd
from sklearn import svm, preprocessing
from sklearn.cluster import KMeans
import numpy as np
from dbManager import DbManager
import datetime


from sklearn import metrics
from scipy.spatial.distance import cdist

import matplotlib.pyplot as plt


class Predictor:
    def __init__(self, typeP):
        self.dbManager = DbManager()
        self.type = typeP
        self.x = None
        self.y = None

    def predict(self, location):
        if self.type == 'Kmeans':
            self.x = self.dbManager.userDB
            self.predictKmeans(location)
        elif self.type == 'svm':
            pass

    def predictKmeans(self, location):
        self.x = self.x.drop(columns=['latitude', 'longitude'])
        self.x = preprocessing.normalize(self.x, norm='l2')
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
        plt.xlabel('Values of K')
        plt.ylabel('Distortion')
        plt.title('The Elbow Method using Distortion')
        plt.show()

        plt.plot(K, inertias, 'bx-')
        plt.xlabel('Values of K')
        plt.ylabel('Inertia')
        plt.title('The Elbow Method using Inertia')
        plt.show()

        print(self.x.mean(axis=0))
        print(self.x.std(axis=0))

        kmeans = KMeans(n_clusters=3, random_state=0).fit(self.x)
        print(kmeans.labels_)
        # kmeans.predict(location)


s = 's'
p = Predictor('Kmeans')
p.predict(s)
