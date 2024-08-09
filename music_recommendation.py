# -*- coding: utf-8 -*-
"""music_recommendation

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J69Tmk5MXUgtBu9C4HkiAvruwKqegm9B
"""

import pandas as pd
import numpy as np
import sklearn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

def load_data():
    df = pd.read_csv("song.csv")
    df.dropna(inplace=True)  # Handle missing values
    return df

df = load_data()
st.title("Music Recommendation System")

# Display summary statistics
st.write("### Summary Statistics")
st.write(df.describe())




songs = df.sample(n=10000).drop('link', axis=1).reset_index(drop=True)


songs['text'] = df['text'].str.replace(r'\n', '')




expert = TfidfVectorizer(analyzer='word', stop_words='english')
text_matrix =expert.fit_transform(songs['text'])


cosine_similarities = cosine_similarity(text_matrix)

similarities = {}

   


# User input for selecting a song
song_index = st.number_input("Select a song index (0-9999):", min_value=0, max_value=9999, value=5)
 

for i in range(len(cosine_similarities)):
    similar_indices = cosine_similarities[i].argsort()[:-3:-1]
    similarities[songs['song'].iloc[i]] = [(songs['song'][x], songs['artist'][x]) for x in similar_indices]
    
st.write(f"### Top 2 Similar Songs to '{songs['song'].iloc[song_index]}'")
for song, artist in similarities[songs['song'].iloc[song_index]]:
    st.write(f"{song} by {artist}")

st.write("### Dataset Preview")
st.dataframe(df.head())
 

    
    














