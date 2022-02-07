import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
from sklearn.preprocessing import LabelEncoder
import sklearn.metrics as sm

place_df = pd.read_csv("website/dataset_place.csv")

#    THE similarity are counted / calculated from the number of similarity of
#    EACH WORDS in place_desc !!!!!!!!!!!!!!!!!!!!!!

tfidf = TfidfVectorizer(stop_words="english")
place_df["place_desc"] = place_df["place_desc"].fillna("")

tfidf_matrix = tfidf.fit_transform(place_df["place_desc"])

# Compute similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(place_df.index, index=place_df["place_name"]).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    """
    in this function,
        we take the cosine score of given PLACE
        sort them based on cosine score (place_id, cosine_score)
        take the next 10 values because the first entry is itself
        get those place indices
        map those indices to place name
        return place name list
    """
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    # (a, b) where a is id of place, b is sim_score

    places_indices = [ind[0] for ind in sim_scores]
    places = place_df["place_name"].iloc[places_indices]
    return places

def get_admission(x):
    for i in x:
        if i["place_admission"] == "free":
            return (i["place_name"])
    return np.nan

def get_list(x):
    if isinstance(x, list):
        names = [i["place_name"] for i in x]

        if len(names) > 3:
            names = names[:3]

        return names

    return []

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ""
        
features = ['place_keyword', 'place_attractions', 'place_admission', 'place_circle']

for feature in features:
    place_df[feature] = place_df[feature].apply(clean_data)
    
def create_soup(x):
    return ' '.join(x['place_keyword']) + ' ' + ' '.join(x['place_attractions'])


place_df["soup"] = place_df.apply(create_soup, axis=1)

#count_vectorizer = CountVectorizer(stop_words="english")

count_vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b", stop_words=None, ngram_range=(2,2), analyzer='word')

count_matrix = count_vectorizer.fit_transform(place_df["soup"])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

place_df = place_df.reset_index()
indices = pd.Series(place_df.index, index=place_df['place_name'])