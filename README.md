# 🎬 MovieMate: The Smart Movie Recommendation System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)]()
[![Contributions Welcome](https://img.shields.io/badge/Contributions-welcome-brightgreen.svg?style=flat)]()

---

## 🌟 Overview

**MovieMate** is an intelligent and interactive **Movie Recommendation System** built using **FastAPI** for the backend and **HTML/CSS/JavaScript** for the frontend.
It combines AI-driven filtering methods and prompt-based intelligence to deliver highly personalized movie suggestions.

Whether you want to discover movies based on your **mood**, **storyline**, or even through **voice commands**, MovieMate has you covered. 🎥✨

---

## 🚀 Features

* 🎬 **Prompt-Based Search** – Search for movies using natural language prompts (e.g., “funny space movies”).
* 🎭 **Mood-Based Recommendation** – Get movie suggestions that match your mood or emotion.
* 🔊 **Voice-Based Search** – Use your voice to find and explore movies.
* 🤝 **Collaborative & Hybrid Filtering** – Smart algorithm combining content and user preference models.
* 📈 **Trending & Social Layer** – See what’s popular among the community.
* 📖 **Storyline-Based Search** – Find movies with similar storylines using NLP.
* ⚡ **FastAPI Backend** – Lightning-fast recommendations powered by Python.
* 💅 **Beautiful Frontend** – Clean and responsive UI built with HTML, CSS, and JavaScript.
* 🖼️ **TMDB API Integration** – Fetches posters, overviews, and movie details.

---

## 🧠 Tech Stack

* **Backend:** Python (FastAPI)
* **Frontend:** HTML, CSS, JavaScript
* **Libraries:** pandas, numpy, scikit-learn, requests
* **Data Files:** `movie_dict.pkl`, `similarity.pkl`
* **API:** TMDB API

---

## 🗂️ Project Structure

```
MovieMate/
│
├── backend/
│   ├── main.py               # FastAPI backend
│   ├── movie_dict.pkl        # Movie data dictionary
│   ├── similarity.pkl        # Similarity matrix
│   ├── data_preprocessing.py # Data update/generation script
│   ├── requirements.txt      # Dependencies
│   └── utils/                # Helper functions (future expansion)
│
├── frontend/
│   ├── index.html            # Frontend interface
│   ├── style.css             # Styling
│   ├── script.js             # Dynamic search & API integration
│   └── assets/               # Icons, images, posters
│
└── README.md                 # Project overview
```

---

## ⚙️ Setup & Run Instructions

### 🧩 Step 1: Clone the Repository

```bash
git clone https://github.com/<your-username>/MovieMate.git
cd MovieMate/backend
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

Your backend server will start at:

```
http://127.0.0.1:8000
```

### 🌐 Step 5: Run Frontend

* Open `frontend/index.html` in your browser or use VS Code Live Server.
* Ensure the backend server is running.
* Search or speak to find movie recommendations instantly 🎬

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

Install them with:

```bash
pip install -r requirements.txt
```

---

# 🤝 How to Contribute

Thank you for your interest in contributing to **MovieMate** — an open-source AI-powered movie recommendation system! 💖
We welcome all kinds of contributions — from fixing bugs 🐞 and improving code 💻 to writing documentation 📚 or suggesting new features 💡.

### 🧭 Steps to Contribute

#### 🪄 1. Fork the Repository

* Click the **“Fork”** button at the top-right of this repo.
* This creates your personal copy of the project.

#### 🌿 2. Clone Your Fork

```bash
git clone https://github.com/<your-username>/MovieMate.git
cd MovieMate
```

#### 🌱 3. Create a New Branch

Create a separate branch for your work:

```bash
git checkout -b feature-name
```

> Example: `git checkout -b add-mood-recommendation`

#### 💻 4. Make Your Changes

* Add your code, tests, or documentation improvements.
* Follow the existing project structure and naming conventions.
* Make sure your code runs without errors.

#### 🧪 5. Test Your Work

Before submitting, test your changes locally to ensure everything works as expected.

#### 📝 6. Commit Your Changes

Use clear and concise commit messages:

```bash
git add .
git commit -m "Added mood-based movie recommendation feature"
```

#### 🚀 7. Push to Your Fork

```bash
git push origin feature-name
```

#### 🔁 8. Create a Pull Request (PR)

* Go to your fork on GitHub.
* Click **“Compare & pull request”**.
* Describe your changes and submit the PR.

---

## 🧩 Areas You Can Contribute To

| Area                                | Description                                 |
| ----------------------------------- | ------------------------------------------- |
| 🧠 Prompt-Based Search              | Improve AI-based movie search prompts.      |
| 🎭 Mood-Based Recommendation        | Enhance emotion-based recommendations.      |
| 🔊 Voice Search                     | Add or improve voice control.               |
| 🔗 Hybrid & Collaborative Filtering | Optimize recommendation algorithms.         |
| 📈 Trending & Social Layer          | Integrate social APIs for trending content. |
| 📖 Storyline Search                 | Improve NLP-based story matching.           |
| 🐞 Bug Fixes                        | Fix UI/UX or backend issues.                |
| 📝 Documentation                    | Enhance setup and usage instructions.       |
| 🎬 Movie Dataset Updates            | Add, clean, or enhance movie data.          |

---

# 🎞️ Contributing Movie Data

MovieMate’s recommendations are powered by movie data stored in `movie_dict.pkl` and `similarity.pkl`.
These files can be **updated, expanded, or replaced** by contributors to include new movies or improve similarity accuracy.

### 🧰 Updating Existing Data

1. Download or clone the repository.
2. Open the `backend/data_preprocessing.py` script (or create one if missing).
3. Add your new movie data (from TMDB API, CSV, etc.).
4. Re-run the script to regenerate `.pkl` files:

   ```bash
   python data_preprocessing.py
   ```
5. Replace old files with the new ones:

   ```bash
   git add backend/movie_dict.pkl backend/similarity.pkl
   git commit -m "Updated movie dataset with 200 new titles"
   ```
6. Push and create a pull request.

### 🌍 Dynamic Data (Future Enhancement)

In future versions, MovieMate will support **dynamic data fetching** from external APIs like TMDB.
That means contributors won’t need to update `.pkl` files manually — the system will fetch new or trending movies automatically.

Example snippet:

```python
import requests
url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}"
movies = [m['title'] for m in requests.get(url).json()['results']]
```

✅ **Short-Term Plan:** Contributors update `.pkl` files manually.
🚀 **Long-Term Vision:** Full API-based dynamic dataset updates.

---

## 🧰 Development Guidelines

* Write **clean, modular, and documented** code.
* Use meaningful commit messages.
* Avoid pushing large files or unnecessary data.
* Test before submitting PRs.

---

## 💬 Communication

If you have questions or ideas:

* Open a new [Issue](../../issues)
* Start a discussion in the **Discussions** tab
* Or comment directly on pull requests

---

## 🌟 Recognition

All contributors will be featured in the **Contributors section** once their PRs are merged.
We truly appreciate your efforts and support! 🙌

---

## 🧩 Future Enhancements

* 🗣️ Integration with GPT-based movie Q&A system
* 📱 Full React.js frontend redesign
* 🌍 Multi-language recommendations
* 💾 User profiles and watch history tracking
* 🎞️ Recommendation visualization dashboard

---

## 👐 Open Source & Community

This project is **open-source** 💻 under the **MIT License**.
Feel free to use, modify, and improve it — just give proper credit.

We encourage everyone to join and collaborate!
Tag your first contribution with **`good first issue`** 🪄

---

## ✨ Author

**Code Catalyst**
*2025 © MovieMate | All Rights Reserved*

> “Movies bring people together. Let’s make discovering them smarter.” 🎬💫
