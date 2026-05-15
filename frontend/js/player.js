const videosContainer = document.getElementById("videos-container");

async function loadVideos() {
  try {
    const response = await fetch(`${API_URL}/videos/`);
    const videos = await response.json();

    videosContainer.textContent = "";

    videos.forEach((video) => {
      const article = document.createElement("article");
      article.className = "video-card";

      const image = document.createElement("img");
      image.src = video.thumbnail_url || "https://via.placeholder.com/400x220";
      image.alt = video.title;

      const content = document.createElement("div");
      content.className = "video-card-content";

      const title = document.createElement("h3");
      title.textContent = video.title;

      const description = document.createElement("p");
      description.textContent = video.description || "Sin descripción";

      const link = document.createElement("a");
      link.href = `player.html?id=${video.id}`;
      link.textContent = "Ver video";

      content.appendChild(title);
      content.appendChild(description);
      content.appendChild(link);

      article.appendChild(image);
      article.appendChild(content);

      videosContainer.appendChild(article);
    });
  } catch (error) {
    videosContainer.textContent = "Error al cargar los videos.";
    console.error(error);
  }
}

loadVideos();