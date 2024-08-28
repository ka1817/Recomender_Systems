import streamlit as st
import pickle
import pandas as pd

def recomend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distences=similarity[movie_index]
    movies_list = sorted(list(enumerate(distences)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity1.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
    'How Would you like to br contacted?',movies['title'].values
)

if st.button('Recommend'):
    recommendations=recomend(selected_movie_name)
    for i in recommendations:
        st.write(i)