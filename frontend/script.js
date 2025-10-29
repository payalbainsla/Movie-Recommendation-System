const apiBase = "http://127.0.0.1:8000/recommend";

document.getElementById("recommendBtn").addEventListener("click", async () => {
  const movieName = document.getElementById("movieInput").value.trim();
  const recommendationsDiv = document.getElementById("recommendations");
  recommendationsDiv.innerHTML = "";

  if (!movieName) {
    recommendationsDiv.innerHTML = "<p>Please enter a movie name!</p>";
    return;
  }

  try {
    const response = await fetch(apiBase, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ movie_name: movieName }),
    });

    if (!response.ok) throw new Error("Backend error");

    const data = await response.json();
    const movies = data.recommended_movies;

    if (!movies.length) {
      recommendationsDiv.innerHTML = "<p>No recommendations found!</p>";
      return;
    }

    movies.forEach((movie) => {
      const movieCard = document.createElement("div");
      movieCard.classList.add("movie-card");
      movieCard.innerHTML = `
        <img src="${movie.poster}" alt="${movie.title}">
        <h3>${movie.title}</h3>
      `;
      recommendationsDiv.appendChild(movieCard);
    });
  } catch (error) {
    console.error(error);
    recommendationsDiv.innerHTML = "<p>Something went wrong. Try again!</p>";
  }
});
