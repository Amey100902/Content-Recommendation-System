import streamlit as st
import pickle
import pandas as pd
import requests
from fuzzywuzzy import fuzz

st.title('Movies Recommendation System')
st.text('Created by: Amey Agrawal')

tmdb_new=pickle.load(open('tmdb_new.pkl','rb'))
movies_list=tmdb_new['title'].values

selected_movie_name = st.selectbox('Select a movie',movies_list)
similarity_score=pickle.load(open('similarity_score.pkl','rb'))

def fetch_page(movie):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path




def recommend(movie):
    closest_match = max(tmdb_new['title'], key=lambda x: fuzz.ratio(x.lower(), movie.lower()))
    movie_index = tmdb_new.index[tmdb_new['title'] == closest_match].tolist()[0]
    distances = similarity_score[movie_index]
    movies_list = sorted((enumerate(distances)),reverse=True,key=lambda x:x[1])[1:10]
    recommended_movies=[]
    recommended_movies_page=[]
    for m in movies_list:
        movie_id = tmdb_new.iloc[m[0]].id
        recommended_movies.append(tmdb_new.iloc[m[0]].title)
        recommended_movies_page.append(fetch_page(movie_id))


    return recommended_movies,recommended_movies_page

if st.button("Recommend similar movies"):
    movie_names,movie_pages=recommend(selected_movie_name)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(movie_names[0])
        st.image(movie_pages[0])
    with col2:
        st.text(movie_names[1])
        st.image(movie_pages[1])

    with col3:
        st.text(movie_names[2])
        st.image(movie_pages[2])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(movie_names[3])
        st.image(movie_pages[3])
    with col2:
        st.text(movie_names[4])
        st.image(movie_pages[4])

    with col3:
        st.text(movie_names[5])
        st.image(movie_pages[5])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(movie_names[6])
        st.image(movie_pages[6])
    with col2:
        st.text(movie_names[7])
        st.image(movie_pages[7])

    with col3:
        st.text(movie_names[8])
        st.image(movie_pages[8])
    