document.addEventListener("DOMContentLoaded", async () => {
  // Fetch blog posts from the backend API
  const response = await fetch("http://127.0.0.1:8000/blogs/");
  const blogs = await response.json();

  // Select the posts grid element to dynamically insert posts
  const postsGrid = document.querySelector(".posts-grid");

  // Clear the current content (if any)
  postsGrid.innerHTML = '';

  // Loop through blogs and display them on the frontend
  blogs.forEach(blog => {
    const postItem = document.createElement('article');
    postItem.classList.add('post-item');

    postItem.innerHTML = `
      <article
        class="grid grid-rows-[300px_auto] md:grid-rows-[300px_220px] min-h-full group">
        <a class="relative overflow-hidden" href="./src/post.html?id=${blog.id}">
          <img
            src="../public/images/${blog.image_url}"
            class="h-full min-w-full object-cover hover:scale-[101%] transition-all duration-200 rounded-[2px]"
            alt="${blog.title}"
            width="600"
            height="200"
            loading="lazy"
            decoding="async"/>
          <div class="z-30 absolute bottom-0 w-full h-20">
            <div
              class="-z-10 absolute bottom-0 glass w-full min-h-full"></div>
            <div
              class="flex items-center justify-between gap-x-1 text-white px-6 py-4">
              <div class="flex flex-col gap-1 items-center justify-center">
                <time
                  class="text-sm font-bold text-opacity-60"
                  datetime="${blog.created_at}">
                  ${new Date(blog.created_at).toLocaleDateString()}
                </time>
                <span class="text-sm"> 4 min read</span>
              </div>
              <span class="pb-4"># ${blog.tags.substring(0, 20)}...</span>
            </div>
          </div>
        </a>
        <div class="flex justify-between flex-col gap-4 md:gap-0 py-6 pl-1">
          <div class="flex flex-col gap-3">
            <div class="flex flex-col gap-2">
              <a
                class="text-2xl font-semibold -tracking-wider"
                href="./src/post.html?id=${blog.id}">
                ${blog.title}
              </a>
            </div>
            <p
              class="overflow-hidden line-clamp-3 text-gray-700 dark:text-white mb-5 font-[400] md:pr-[15%]">
              ${blog.content.substring(0, 100)}...
            </p>
          </div>
          <footer class="flex justify-between items-center">
            <a
              href="./src/post.html?id=${blog.id}"
              class="flex justify-center items-center dark:text-white rounded-full hover:translate-x-1 transition-transform duration-150 ease-in-out font-semibold gap-1 group"
              aria-label="go to ${blog.title}">
              Read Post
              <span
                class="mt-[1px] group-hover:rotate-45 transition-transform duration-250 ease-in-out"
                ><svg
                  class="feather feather-arrow-up-right"
                  fill="none"
                  height="18"
                  stroke="currentColor"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2.5"
                  viewBox="0 0 24 24"
                  width="18"
                  xmlns="http://www.w3.org/2000/svg">
                  <line x1="7" x2="17" y1="17" y2="7"></line>
                  <polyline points="7 7 17 7 17 17"></polyline></svg
              ></span>
            </a>
          </footer>
        </div>
      </article>
    `;
    postsGrid.appendChild(postItem);
  });
});
