# 🎬 MovieMate: A Movie Recommendation System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A powerful **Movie Recommendation System** built using **FastAPI** (for backend) and **HTML/CSS/JS** (for frontend).
It recommends movies similar to the one selected by the user using **content-based filtering** and other intelligent features.

---

## 🚀 Features

* 🎥 **Similar Movie Recommendations** based on cosine similarity.
* 🧠 **Prompt-Based Search** – Search movies with natural language queries (e.g., “funny space adventure”).
* 💬 **Storyline-Based Search** – Recommend movies based on story or description.
* 😄 **Mood-Based Recommendations** – Suggest movies based on mood or emotions.
* 🎤 **Voice-Based Search** – Search movies using your voice.
* 🔥 **Trending & Social Layer** – Display popular and trending movies.
* 🎬 **Movie Overview Feature** – Shows a short description, rating, genre, and cast using **OMDb API**.
* 🔄 **Hybrid & Collaborative Filtering** – Combine user and content preferences for better recommendations.
* 💾 **Dynamic Data Updating** – Contributors can add or update movie data for continuous improvement.
* ⚡ Backend powered by FastAPI with instant responses.
* 💅 Clean, responsive frontend built with HTML & CSS.

---

## 🧠 Tech Stack

* **Backend:** Python (FastAPI)
* **Frontend:** HTML, CSS, JavaScript
* **Libraries:** pandas, numpy, scikit-learn, requests
* **API:** [OMDb API](https://www.omdbapi.com/) for fetching movie details & overviews
* **Data Files:** `movie_dict.pkl`, `similarity.pkl`

---

## 🗂️ Project Structure

```
Movie-Recommendation-System/
│
├── backend/
│   ├── main.py               # FastAPI backend
│   ├── movie_dict.pkl        # Movie data dictionary
│   ├── similarity.pkl        # Similarity matrix
│   ├── requirements.txt      # Dependencies
│   └── data_preprocessing.py # For dataset updates
│
├── frontend/
│   ├── index.html            # Home page
│   ├── recommendation.html   # Recommendation page
│   ├── favourites.html       # Favourite movies page
│   ├── about.html            # About project page
│   ├── style.css             # Styling
│   └── script.js             # Frontend interactivity
│
└── README.md
```

---

## ⚙️ Setup & Run Instructions

### 🧩 Step 1: Clone the Repository

```bash
git clone https://github.com/<your-username>/Movie-Recommendation-System.git
cd Movie-Recommendation-System/backend
```

### 🧠 Step 2: Create & Activate Virtual Environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 📦 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔑 Step 4: Setup OMDb API Key

1. Visit [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx) and get your free API key.
2. Add it to your `.env` file or directly in your code:

```python
OMDB_API_KEY = "your_api_key_here"
```

### 🚀 Step 5: Run the FastAPI Server

```bash
uvicorn main:app --reload
```

When it starts, you’ll see something like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## 🌐 Step 6: Run Frontend

* Open `frontend/index.html` in your browser.
* Make sure the backend (FastAPI server) is running.
* Search or select a movie → get recommendations instantly 🎬

---

## 🔗 Example API Endpoint

```
GET http://127.0.0.1:8000/recommend?movie=Inception
```

Response:

```json
{
  "recommended_movies": [
    "Interstellar",
    "The Dark Knight",
    "Tenet",
    "Memento",
    "The Prestige"
  ]
}
```

---

## 📦 Dependencies

```
fastapi
uvicorn
scikit-learn
pandas
numpy
requests
python-dotenv
```

Install all via:

```bash
pip install -r requirements.txt
```

---

## 🧩 Contributing

We welcome contributions from everyone 💡!
Here’s how you can help:

### 🔹 How to Contribute

1. **Fork** this repository to your GitHub account.
2. **Clone** your fork locally and create a new branch.
3. **Make changes** — improve code, fix bugs, add features.
4. **Commit and push** your branch.
5. **Create a Pull Request (PR)** to the main repository.
6. Wait for review & merge approval.

You don’t need main repo access — all changes go via PRs ✅.

### 🔹 Areas to Contribute

* 🧠 **Prompt-Based Search** – Improve NLP query understanding.
* 🎭 **Mood-Based Recommendations** – Enhance emotion recognition.
* 🎤 **Voice Search** – Add multi-language or improved recognition.
* 🔗 **Hybrid & Collaborative Filtering** – Tune algorithms for better accuracy.
* 🎬 **Movie Overview Feature** – Improve OMDb integration to show cast, genre, poster, and ratings.
* 💾 **Dataset Enhancement** – Add new movies or update metadata.
* 🧩 **Frontend Pages** – Complete or improve following pages:

  * **Home Page:** Search bar and intro (already functional).
  * **Recommendation Page:** Show recommended movies with overviews, trailers, and ratings.
  * **Favourites Page:** Save and manage liked movies.
  * **About Page:** Add project details, team info, and API credits.
* 🧪 **Testing & Bug Fixes** – Test features and fix UI/backend issues.

---

## 🎥 Contributing Movie Data

Contributors can also help improve or expand the movie dataset:

### 📁 Updating Movie Data

1. Modify or replace `movie_dict.pkl` and `similarity.pkl` using `data_preprocessing.py`.
2. Generate new files locally and test recommendations.
3. Commit the updated files and open a pull request.

Example:

```bash
python data_preprocessing.py
git add backend/movie_dict.pkl backend/similarity.pkl
git commit -m "Updated dataset with 100 new movies"
git push
```

### 🔄 Future Plan: Dynamic Movie Data

We plan to shift to **OMDb API-based live fetching**, so data always stays up-to-date without manual updates.

---

## 👐 Open Source

This project is **open-source** 💻
Feel free to use, modify, and improve it with proper credits.
Pull requests are welcome!

---

## ✨ Author

**Code Catalyst**
Movie Recommendation System | 2025
