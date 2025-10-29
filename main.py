from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import pickle
import os
import requests

# Create app instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # or ["http://127.0.0.1:5500"] if using Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model
class MovieRequest(BaseModel):
    movie_name: str

# Get current directory path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load data
movie_dict = pickle.load(open(os.path.join(BASE_DIR, 'movie_dict.pkl'), 'rb'))
similarity = pickle.load(open(os.path.join(BASE_DIR, 'similarity.pkl'), 'rb'))
movies = pd.DataFrame(movie_dict)

# OMDb API key and base URL
OMDB_API_KEY = "2052fcca"
OMDB_BASE_URL = "http://www.omdbapi.com/"

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_title = movies.iloc[i[0]].title

        # Fetch poster from OMDb
        params = {"t": movie_title, "apikey": OMDB_API_KEY}
        response = requests.get(OMDB_BASE_URL, params=params)
        data = response.json()

        poster_url = data.get("Poster", "https://via.placeholder.com/300x450?text=No+Poster")

        recommended_movies.append({
            "title": movie_title,
            "poster": poster_url
        })

    return recommended_movies

# Routes
@app.get("/")
def home():
    return {"message": "Welcome to the Movie Recommendation API!"}

@app.post("/recommend")
def recommend_movies(request: MovieRequest):
    movie_name = request.movie_name
    recommendations = recommend(movie_name)
    return {"recommended_movies": recommendations}
