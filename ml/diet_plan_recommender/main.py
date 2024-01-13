import pandas as pd
import numpy as np
import sklearn
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
import warnings
import time
import seaborn as sns
import matplotlib.pyplot as plt
import random
import nltk
from nltk.corpus import stopwords

warnings.filterwarnings('ignore')

df = pd.read_csv('dataset.csv')


class Recommender:

    def __init__(self):
        self.df = pd.read_csv('dataset.csv')

    def get_features(self):
        # getting dummies of dataset
        nutrient_dummies = self.df.Nutrient.str.get_dummies()
        disease_dummies = self.df.Disease.str.get_dummies(sep=' ')
        diet_dummies = self.df.Diet.str.get_dummies(sep=' ')
        feature_df = pd.concat([nutrient_dummies, disease_dummies, diet_dummies], axis=1)

        return feature_df

    def k_neighbor(self, inputs):
        feature_df = self.get_features()

        # initializing model with k=20 neighbors
        model = NearestNeighbors(n_neighbors=40, algorithm='ball_tree')

        # fitting model with dataset features
        model.fit(feature_df)

        df_results = pd.DataFrame(columns=list(self.df.columns))

        # getting distance and indices for k nearest neighbor
        distnaces, indices = model.kneighbors(inputs)

        for i in list(indices):
            df_results = df_results._append(self.df.loc[i])

        df_results = df_results.filter(
            ['Name', 'Nutrient', 'Veg_Non', 'Price', 'Review', 'Diet', 'Disease', 'description'])
        df_results = df_results.drop_duplicates(subset=['Name'])
        df_results = df_results.reset_index(drop=True)
        return df_results


ob = Recommender()
data = ob.get_features()

total_features = data.columns
d = dict()
for i in total_features:
    d[i]= 0
print(d)    # not needed

sample_input = ['high_protien_diet', 'gluten_free_diet', 'diabeties', 'anemia', 'calcium', 'protien']

for i in sample_input:
    d[i] = 1

final_input = list(d.values())
