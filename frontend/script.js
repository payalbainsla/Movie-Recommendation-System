document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("movieInput");
  const btn = document.getElementById("recommendBtn");
  const recommendations = document.getElementById("recommendations");
  const navLinks = document.querySelectorAll(".nav ul li a");

  // 🎬 Navbar active animation
  navLinks.forEach(link => {
    link.addEventListener("click", () => {
      navLinks.forEach(l => l.classList.remove("active"));
      link.classList.add("active");
    });
  });

  // 🎞 Search button click
  btn.addEventListener("click", async () => {
    const movieName = input.value.trim();
    if (!movieName) return alert("Please enter a movie name!");

    recommendations.innerHTML = `<p style="color:#aaa;text-align:center;">Loading recommendations...</p>`;

    try {
      const res = await fetch(`https://www.omdbapi.com/?s=${movieName}&apikey=564727fa`);
      const data = await res.json();

      if (data.Response === "False") {
        recommendations.innerHTML = `<p style="color:#E50914;text-align:center;">No movies found. Try another name!</p>`;
        return;
      }

      recommendations.innerHTML = "";

      data.Search.forEach(movie => {
        let poster = movie.Poster && movie.Poster !== "N/A"
          ? movie.Poster
          : "https://via.placeholder.com/300x450/000000/FFFFFF?text=No+Poster";

        const movieCard = document.createElement("div");
        movieCard.classList.add("movie-card");

        movieCard.innerHTML = `
          <img src="${poster}" alt="${movie.Title}">
          <h3>${movie.Title}</h3>
          <p>${movie.Year}</p>
        `;

        // ✅ Fallback in case poster URL is broken (404 or invalid)
        const img = movieCard.querySelector("img");
        img.onerror = () => {
          img.src = "https://via.placeholder.com/300x450/000000/FFFFFF?text=No+Poster";
        };

        // ✨ Smooth fade-in
        movieCard.style.opacity = "0";
        recommendations.appendChild(movieCard);
        requestAnimationFrame(() => {
          movieCard.style.transition = "opacity 0.6s ease-in";
          movieCard.style.opacity = "1";
        });
      });
    } catch (error) {
      console.error(error);
      recommendations.innerHTML = `<p style="color:#E50914;text-align:center;">Error fetching movies. Try again later.</p>`;
    }
  });
});
