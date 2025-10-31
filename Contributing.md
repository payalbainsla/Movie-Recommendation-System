# 🤝 Contributing to MovieMate

Welcome to **MovieMate** — an open-source AI-powered movie recommendation system! 🎬
We’re thrilled that you’re interested in contributing. Every contribution — big or small — helps us make this project smarter, faster, and more useful for everyone.

---

## 🧭 How You Can Contribute

There are many ways to contribute:

* 💡 Suggest new features or improvements
* 🐞 Report and fix bugs
* 🧠 Work on AI models (hybrid filtering, mood detection, etc.)
* 🎨 Improve frontend design or user experience
* 📝 Write or improve documentation

---

## ⚙️ Contribution Process

### 1️⃣ Fork the Repository

Click the **“Fork”** button at the top-right of this page to create your own copy of the repo.

### 2️⃣ Clone Your Fork

```bash
git clone https://github.com/<your-username>/MovieMate.git
cd MovieMate
```

### 3️⃣ Create a New Branch

Always create a new branch for your feature or fix:

```bash
git checkout -b feature-name
```

> Example: `git checkout -b add-mood-based-recommendation`

### 4️⃣ Make Your Changes

Add your improvements in your local environment.
Follow good coding practices and comment your code clearly.

### 5️⃣ Test Your Changes

Before submitting your code, make sure:

* The app runs without errors
* Your new feature or fix works as expected
* You haven’t broken existing functionality

### 6️⃣ Commit and Push

```bash
git add .
git commit -m "Added mood-based movie recommendation feature"
git push origin feature-name
```

### 7️⃣ Create a Pull Request

* Go to your fork on GitHub.
* Click **“Compare & pull request”**.
* Add a clear title and description of your changes.
* Submit the pull request (PR).

We’ll review it and provide feedback before merging. 💬

---

## 🧩 Contribution Areas

| Area                                | Description                                         |
| ----------------------------------- | --------------------------------------------------- |
| 🧠 Prompt-Based Search              | Improve the search system using AI-based prompts.   |
| 🎭 Mood-Based Recommendation        | Suggest movies based on emotional tone or mood.     |
| 🔊 Voice Search                     | Add or improve voice command features.              |
| 🔗 Hybrid & Collaborative Filtering | Enhance recommendation algorithms.                  |
| 📈 Trending & Social Layer          | Add trending or social media-based recommendations. |
| 📖 Storyline Search                 | Implement NLP to understand movie plots.            |
| 🐞 Bug Fixes                        | Fix errors or performance issues.                   |
| 📝 Documentation                    | Improve README, setup guides, or examples.          |

---

## 💻 Development Setup

### Backend (FastAPI)

```bash
pip install -r requirements.txt
uvicorn Backend.main:app --reload
```

### Frontend

Open `index.html` in your browser or use VS Code Live Server.

---

## 🧰 Code Guidelines

* Write clean, modular, and documented code.
* Follow consistent naming conventions.
* Avoid pushing unnecessary files (check `.gitignore`).
* Make focused, small pull requests.

---

## 💬 Communication

If you have questions or ideas:

* Open a new [Issue](../../issues)
* Start a discussion in the **Discussions** tab
* Or comment directly on pull requests

---

## 🌟 Recognition

Your name will appear in our **Contributors** section after your PR is merged.
We truly appreciate your efforts and support! 🙌

---

## ⚖️ License

By contributing, you agree that your code will be licensed under the same license as this project — **MIT License**.

---

Thank you for helping us make **MovieMate** better! 🎥✨
Let’s build the future of movie recommendations — together. 💫
