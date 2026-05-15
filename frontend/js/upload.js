const form = document.getElementById("upload-form");
const message = document.getElementById("upload-message");

form.addEventListener("submit", async (e) => {

  e.preventDefault();

  const formData = new FormData();

  formData.append(
    "title",
    document.getElementById("title").value
  );

  formData.append(
    "description",
    document.getElementById("description").value
  );

  formData.append(
    "user_id",
    document.getElementById("user-id").value
  );

  formData.append(
    "category_id",
    document.getElementById("category-id").value
  );

  formData.append(
    "video_file",
    document.getElementById("video-file").files[0]
  );

  formData.append(
    "thumbnail_file",
    document.getElementById("thumbnail-file").files[0]
  );

  try {

    message.textContent = "Subiendo video...";

    const response = await fetch(
      `${API_URL}/videos/upload`,
      {
        method: "POST",
        body: formData
      }
    );

    if (!response.ok) {
      throw new Error("Error al subir el video");
    }

    message.textContent = "Video subido correctamente.";

    form.reset();

  } catch (error) {

    console.error(error);

    message.textContent = "No se pudo subir el video.";
  }

});