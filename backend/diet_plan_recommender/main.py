import warnings

import pandas as pd
from nltk.corpus import stopwords
from sklearn.neighbors import NearestNeighbors

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


class Profile:
    df = pd.read_csv('dataset.csv')  # static variable

    def __init__(self, diet, disease, Nutrient, food_type, favorite_food):
        self.diet = diet
        self.disease = disease
        self.nutrient = Nutrient
        self.type = food_type
        self.like = favorite_food
        self.df2 = pd.DataFrame(columns=list(Profile.df.columns))
        self.df3 = pd.DataFrame(columns=list(Profile.df.columns))
        self.df4 = pd.DataFrame(columns=list(Profile.df.columns))
        self.df5 = pd.DataFrame(columns=list(Profile.df.columns))
        self.df6 = pd.DataFrame(columns=list(Profile.df.columns))

    def removestop(self, tokens):
        stop = set(stopwords.words('english'))
        file = open('stopwords.txt', 'r')
        l = list(file.read().split())
        stop = list(stop) + l
        l = [token for token in tokens if token not in stop]
        return l

    def inputs(self, diet, disease, Nutrient, food_type, favorite_food):

        if Nutrient:
            self.df2 = Profile.df[Profile.df.Nutrient.isin(Nutrient)]
            self.df2 = self.df2.reset_index()

        if food_type:
            self.df2 = self.df2[self.df2.Veg_Non.isin(food_type)]
            self.df2 = self.df2.reset_index()

        if diet:
            for i in range(self.df2.shape[0]):
                l = str(self.df2.loc[i, 'Diet']).split()

                for d in diet:
                    if d in l:
                        self.df4 = self.df4._append(self.df2.loc[i])

        if disease:
            for i in range(self.df2.shape[0]):
                l = str(self.df2.loc[i, 'Disease']).split()
                for d in disease:
                    if d in l:
                        self.df5 = self.df5._append(self.df2.loc[i])

        if favorite_food:
            f = self.removestop(favorite_food.split())
            for i in range(Profile.df.shape[0]):
                n = [j.lower() for j in str(Profile.df.loc[i, 'Name']).split()]
                for j in n:
                    for k in f:
                        if k == j:
                            self.df6 = self.df6._append(Profile.df.loc[i])
            for i in range(Profile.df.shape[0]):
                n = [j.lower() for j in str(Profile.df.loc[i, 'description']).split()]
                for j in n:
                    for k in f:
                        if k == j:
                            self.df6 = self.df6._append(df.loc[i])
            for i in range(Profile.df.shape[0]):
                n = [j.lower() for j in str(Profile.df.loc[i, 'catagory']).split()]
                for j in n:
                    for k in f:
                        if k == j:
                            self.df6 = self.df6._append(Profile.df.loc[i])

        return self.df2, self.df3, self.df4, self.df5, self.df6

    def get_profile(self):
        df2, df3, df4, df5, df6 = self.inputs(self.diet, self.disease, self.nutrient, self.type, self.like)

        df_merge = pd.concat([df2, df3, df4, df5, df6], axis=0).drop_duplicates(subset='Name')
        df_merge = df_merge.filter(['Name', 'Nutrient', 'Veg_Non', 'Price', 'Review', 'description'])
        print(df_merge.shape)

        return df_merge


# ['low_sodium_diet','low_fat_diet'], ['diabeties'], ['calcium','vitamin_c'], ['non-veg'],'i love indian'
def get_meal_plan(diet, disease, nutrient, food_type, favorite_food):
    ob = Profile(diet, disease, nutrient, food_type, favorite_food)
    profile = ob.get_profile()
    return profile
