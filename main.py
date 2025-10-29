from fastapi import FastAPI
from pydantic import BaseModel 
import pandas as pd
import pickle
import os
  
#creating app instance
app = FastAPI()  

class MovieRequest(BaseModel):
    movie_name: str  
     
def _init_(self, movie_name):     
    self.movie_name = movie_name   
    
# Get current directory path 
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 

# Load files 
movie_dict = pickle.load(open('movie_dict.pkl', 'rb')) 
similarity = pickle.load(open(os.path.join(BASE_DIR, "similarity.pkl"), "rb")) 
movies = pd.DataFrame(movie_dict)                           

#recommendation function 
def recommend(movie):     
    movie_index = movies[movies['title'] == movie].index[0]     
    distances = similarity[movie_index]     
    movie_dict = sorted(list(enumerate(distances)), reverse = True, key=lambda x:x[1])[1:6]      
    
    recommended_movies = []     
    for i in movie_dict:         
        recommended_movies.append(movies.iloc[i[0]].title)      
    return recommended_movies  

#get route 
@app.get('/') 
def home():     
    return ('message : Welcome to the Movie recommendation API!')  

#recommend route 
@app.post('/recommend') 
def recommend_movies(request:MovieRequest):     
    movie_name = request.movie_name     
    recommendations = recommend(movie_name)     
    return {'recommended_movies': recommendations}