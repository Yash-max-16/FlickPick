import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4718210e2105b2a55fa99fe9f2fe4daf'.format(movie_id))
    movie_details = response.json()
    poster_link = 'https://image.tmdb.org/t/p/w185/' + movie_details['poster_path']
    return poster_link

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=(lambda x: x[1]))[1:6]
    recommend_movies_list = []
    recommend_movies_posters_list = []
    for movie in movies_list:
        movie_id = movies.iloc[movie[0]].movie_id
        # storing the recommended movie title
        recommend_movies_list.append(movies.iloc[movie[0]].title)
        # fetching the movie poster from API
        poster_link = fetch_poster(movie_id)
        recommend_movies_posters_list.append(poster_link)
    return recommend_movies_list, recommend_movies_posters_list

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
# write some comments
st.title('Movies Recommender')
user_selected_movie = st.selectbox(
    'Select your movie',
    movies['title'].values
)
if st.button('Recommend'):
    names,posters = recommend(user_selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(names[0])
        st.image(posters[0])
    with col2:
        st.write(names[1])
        st.image(posters[1])
    with col3:
        st.write(names[2])
        st.image(posters[2])
    with col4:
        st.write(names[3])
        st.image(posters[3])
    with col5:
        st.write(names[4])
        st.image(posters[4])