# 🎬 MovieMate: A Movie Recommendation System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


A simple **Movie Recommendation System** built using **FastAPI** (for backend) and **HTML/CSS** (for frontend).  
It recommends movies similar to the one selected by the user using **content-based filtering**.

---

## 🚀 Features
- 🎥 Recommends similar movies based on cosine similarity.
- ⚡ Backend powered by FastAPI.
- 💅 Frontend built with HTML & CSS.
- 🖼️ Fetches movie posters using TMDB API.
- 🔄 Instant results with interactive UI.

---

## 🧠 Tech Stack
- **Backend:** Python (FastAPI)
- **Frontend:** HTML, CSS
- **Libraries:** pandas, numpy, scikit-learn, requests
- **Data Files:** `movie_dict.pkl`, `similarity.pkl`

---

## 🗂️ Project Structure
```
Movie-Recommendation-System/
│
├── backend/
│   ├── main.py               # FastAPI backend
│   ├── movie_dict.pkl        # Movie data dictionary
│   ├── similarity.pkl        # Similarity matrix
│   └── requirements.txt      # Dependencies
│
├── frontend/
│   ├── index.html            # Frontend interface
│   ├── style.css             # Styling
│   └── script.js             # Optional JS (if used)
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

### 🚀 Step 4: Run the FastAPI Server
```bash
uvicorn main:app --reload
```

When it starts, you’ll see something like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## 🌐 Step 5: Run Frontend
- Open `frontend/index.html` in your browser.
- Make sure the backend (FastAPI server) is running.
- Search or select a movie → get recommendations instantly 🎬

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
```

Install all via:
```bash
pip install -r requirements.txt
```

---

## 👐 Open Source
This project is **open-source** 💻  
Feel free to use, modify, and improve it with proper credits.  
Pull requests are welcome!

---

## ✨ Author
**Code Catalyst**  
Movie Recommendation System | 2025  




