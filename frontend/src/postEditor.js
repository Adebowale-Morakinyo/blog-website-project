// Image preview functionality
document.getElementById("image").addEventListener("change", function (e) {
  const file = e.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      const preview = document.getElementById("imagePreview");
      preview.src = e.target.result;
      preview.classList.remove("d-none");
    };
    reader.readAsDataURL(file);
  }
});

// Helper function to save image to frontend/public/images
async function saveImageToPublic(imageFile) {
  if (!imageFile) return null;

  try {
    const formData = new FormData();
    formData.append("image", imageFile);

    const response = await fetch("http://127.0.0.1:8000/blogs/upload-image/", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      console.error("Image upload failed:", response.statusText);
      throw new Error("Failed to upload image");
    }

    const result = await response.json();
    return result.filename;
  } catch (error) {
    console.error("Error uploading image:", error);
    throw error;
  }
}

// Form submission
document
  .getElementById("blogForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    try {
      const imageFile = document.getElementById("image").files[0];
      let imageUrl = "";

      if (imageFile) {
        imageUrl = await saveImageToPublic(imageFile);
      }

      const formData = {
        title: document.getElementById("title").value,
        content: document.getElementById("content").value,
        image_url: imageUrl,
        tags: document.getElementById("tags").value,
      };

      // console.log("Form data being sent:", JSON.stringify(formData, null, 2));

      const blog_response = await fetch("http://127.0.0.1:8000/blogs/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      // console.log("Response status:", blog_response.status);
      // console.log("Response headers:", blog_response.headers);

      if (blog_response.ok) {
        try {
          const result = await blog_response.json();
          // console.log("Response JSON:", result); // Debugging response JSON
          window.location.href = `./post.html?id=${result.id}`;
        } catch (jsonError) {
          console.error("Failed to parse JSON response:", jsonError);
          alert("Failed to process the server response. Please try again.");
        }
      } else {
        const errorText = await blog_response.text();
        console.error("Error response text:", errorText);
        throw new Error(`Failed with status: ${blog_response.status}`);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to create blog post. Please try again.");
    }
  });
