import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

st.title('🎬 Content-Based Movie Recommender')
st.write("Select a movie you enjoyed, and we will recommend 5 similar titles based on their plot, genres, and keywords!")

@st.cache_data
def load_data():
    with open('movie_list.pkl', 'rb') as file:
        movies = pickle.load(file)
    with open('similarity_matrix.pkl', 'rb') as file:
        similarity_matrix = pickle.load(file)
    return movies, similarity_matrix

try:
    movies, similarity_matrix = load_data()
except FileNotFoundError:
    st.error("Error: Pickle files not found. Please run the Task 4 script to generate them.")
    st.stop()
def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity_matrix[movie_index]
    sorted_scores = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)
    top_items = sorted_scores[1:6]

    recommended_movies = []
    for item in top_items:
        movie_idx = item[0]
        recommended_movies.append(movies.iloc[movie_idx]['title'])
        
    return recommended_movies

selected_movie = st.selectbox(
    "Search or select a movie from the dropdown:",
    movies['title'].values
)

if st.button('Show Recommendations'):
    with st.spinner('Finding the best matches...'):
        recommendations = recommend(selected_movie)
        
    st.subheader(f"Because you liked '{selected_movie}', we recommend:")
    
    for i, movie_title in enumerate(recommendations, 1):
        st.write(f"**{i}.** {movie_title}")
        
st.markdown("---")
st.caption("Built with using Python and Streamlit")