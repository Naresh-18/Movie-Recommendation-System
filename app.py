import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

st.header('Movie Recommender System')

# Load the movie list and similarity data
movies = pickle.load(open('Movie_reccomendation/movie_list.pkl', 'rb'))
similarity = pickle.load(open('Movie_reccomendation/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Custom HTML for the movie grid
    html_code = f"""
    <div style="display: flex; justify-content: space-around; margin-top: 20px;">
        <div style="text-align: center; margin-right: 10px;">
            <img src="{recommended_movie_posters[0]}" style="width: 150px; border-radius: 10px;">
            <h3 style="font-size: 16px; color: #ffffff;">{recommended_movie_names[0]}</h3>
        </div>
        <div style="text-align: center; margin-right: 10px;">
            <img src="{recommended_movie_posters[1]}" style="width: 150px; border-radius: 10px;">
            <h3 style="font-size: 16px; color: #ffffff;">{recommended_movie_names[1]}</h3>
        </div>
        <div style="text-align: center; margin-right: 10px;">
            <img src="{recommended_movie_posters[2]}" style="width: 150px; border-radius: 10px;">
            <h3 style="font-size: 16px; color: #ffffff;">{recommended_movie_names[2]}</h3>
        </div>
        <div style="text-align: center; margin-right: 10px;">
            <img src="{recommended_movie_posters[3]}" style="width: 150px; border-radius: 10px;">
            <h3 style="font-size: 16px; color: #ffffff;">{recommended_movie_names[3]}</h3>
        </div>
        <div style="text-align: center;">
            <img src="{recommended_movie_posters[4]}" style="width: 150px; border-radius: 10px;">
            <h3 style="font-size: 16px; color: #ffffff;">{recommended_movie_names[4]}</h3>
        </div>
    </div>
    """

    st.components.v1.html(html_code, height=320)
