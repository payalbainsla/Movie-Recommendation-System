from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
import os

#creating app instance
app = FastAPI(title="Movie Recommendation System")

#get current directory path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#load saved data
movies_dict = pickle.load(open(os.path.join(BASE_DIR, "movie_dict.pkl"),"rb"))
similarity = pickle.load(open(os.path.join(BASE_DIR, "similarity.pkl"),"rb"))
movies = pd.DataFrame(movies_dict)
#recommendation function
def recommend(movie): 
    movie_index = [movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_dict = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])
    
    recommended_movies = []
    for i in movies_dict[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

#get route
@app.get('/')
def home():
    return('message : Welcome to the movie recommendationj API')

#recommend route
@app.post('/recommend')
def recommend_movies(request:MovieRequest):
    movie_name = request.movie_name
    recommendations = recommend(movie_name)
    return{"recommended_movies" : recommendations}