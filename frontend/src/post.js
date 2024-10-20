document.addEventListener("DOMContentLoaded", async () => {
    const urlParams = new URLSearchParams(window.location.search);
    const postId = urlParams.get("id");
  
    if (postId) {
      try {
        // Fetch the blog post from the backend API
        const response = await fetch(`http://127.0.0.1:8000/blogs/${postId}`);
        const blog = await response.json();
  
        // Update the page with the blog details
        document.querySelector(".post-title").textContent = blog.title;
        document.querySelector(".post-date").textContent = new Date(blog.created_at).toLocaleDateString("en-US", {
          year: "numeric",
          month: "short",
          day: "numeric"
        });
        document.querySelector(".post-content").textContent = blog.content;
  
        // Update image
        document.querySelector(".post-image").src = `../public/images/${blog.image_url || 'placeholder.jpg'}`;
  
        // Populate tags
        const tagsContainer = document.querySelector(".post-tags");
        tagsContainer.innerHTML = ''; // Clear existing tags if any
  
        const tags = blog.tags ? blog.tags.split(",") : [];
        tags.forEach(tag => {
          const tagElement = document.createElement("span");
          tagElement.className = "bg-indigo-600 font-semibold text-white dark:bg-indigo-900 dark:text-white shadow text-sm w-fit px-2 py-1 md:px-5 md:py-2 rounded-full";
          tagElement.textContent = tag.trim();
          tagsContainer.appendChild(tagElement);
        });
      } catch (error) {
        console.error("Error fetching blog post:", error);
      }
    }
  });
