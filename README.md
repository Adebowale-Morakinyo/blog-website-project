# **🌟 Group E Blog Website**

Welcome to **Group E Blog Website**, a fully functional blog platform where users can explore blog posts, read detailed articles, and create new posts with tags and featured images. This project showcases modern web development practices, including a dynamic UI, a RESTful backend, and seamless frontend-backend integration.

---

## **🚀 Features**

- 📝 **Dynamic Blog Listing**: View a list of all blog posts on the homepage.
- 📖 **Detailed Blog View**: Click on any blog to read the full post with its tags and featured image.
- ✍️ **Create Blog Posts**: Users can create and publish new blog posts with:
  - Title, content, tags, and featured images.
- 🏷️ **Tags Support**: Blog posts can include multiple tags for easy categorization.
- 🌐 **Responsive UI**: Optimized for desktop and mobile devices.
- 🎨 **Dynamic Images**: Preview images before uploading and display them across the platform.

---

## **🛠️ Technologies Used**

### **Frontend**:
- **HTML5**: Markup for structuring the UI.
- **CSS3**: Styling with Bootstrap and custom classes for responsiveness.
- **JavaScript**: Dynamic functionality, including image previews and data fetching.

### **Backend**:
- **FastAPI**: A modern Python framework for creating RESTful APIs.
- **SQLAlchemy**: ORM for managing the SQLite database.
- **Pydantic**: Data validation and schema generation.
- **Shutil**: File handling for image uploads.

### **Database**:
- **SQLite**: Lightweight, file-based relational database.

### **Other Tools**:
- **Bootstrap**: For a responsive and modern UI.
- **Postman**: For API testing during development.

---

## **📂 Project Structure**

```plaintext
/blog-website-project/
│
├── frontend/
│   ├── public/                   # Static images folder
│   │   └── images/
│   ├── src/
│   │   ├── index.html            # Homepage for blog listing
│   │   ├── post.html             # Page for individual blog posts
│   │   ├── post-editor.html      # Page for creating a blog post
│   │   ├── styles.css            # Main CSS file
│   │   └── scripts.js            # Main JavaScript file
│   └── .gitignore                # Ignore unnecessary frontend files
│
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI entry point
│   │   ├── models.py             # Database models
│   │   ├── schemas.py            # Pydantic schemas
│   │   ├── database.py           # Database connection logic
│   │   ├── crud.py               # CRUD operations
│   │   ├── routers/
│   │   │   └── blog_router.py    # API routes for blog CRUD
│   ├── tests/                    # Backend test cases (optional)
│   └── requirements.txt          # Python dependencies
│
├── .gitignore                    # Ignore unnecessary files in the root
├── README.md                     # Project documentation
└── docker-compose.yml            # Optional: Docker setup for deployment
```

---

## **📄 API Documentation**

### **Base URL**: `http://127.0.0.1:8000/blogs/`

### **Endpoints**:

#### **1. Get All Blogs**
- **URL**: `/`
- **Method**: `GET`
- **Description**: Fetch a list of all blogs.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "title": "Blog Title",
      "content": "Blog content",
      "image_url": "image.jpg",
      "tags": "Tag1, Tag2",
      "created_at": "2024-10-18T12:34:56Z",
      "updated_at": "2024-10-18T12:34:56Z"
    }
  ]
  ```

#### **2. Create a New Blog**
- **URL**: `/`
- **Method**: `POST`
- **Description**: Create a new blog post.
- **Request Body**:
  ```json
  {
    "title": "My Blog Title",
    "content": "Blog content goes here...",
    "image_url": "image.jpg",
    "tags": "Tag1, Tag2"
  }
  ```
- **Response**:
  ```json
  {
    "id": 2,
    "title": "My Blog Title",
    "content": "Blog content goes here...",
    "image_url": "image.jpg",
    "tags": "Tag1, Tag2",
    "created_at": "2024-10-18T12:34:56Z",
    "updated_at": "2024-10-18T12:34:56Z"
  }
  ```

#### **3. Get a Single Blog**
- **URL**: `/{blog_id}`
- **Method**: `GET`
- **Description**: Fetch details of a specific blog post.
- **Response**:
  ```json
  {
    "id": 1,
    "title": "Blog Title",
    "content": "Blog content",
    "image_url": "image.jpg",
    "tags": "Tag1, Tag2",
    "created_at": "2024-10-18T12:34:56Z",
    "updated_at": "2024-10-18T12:34:56Z"
  }
  ```

#### **4. Upload an Image**
- **URL**: `/upload-image/`
- **Method**: `POST`
- **Description**: Upload an image file for a blog post.
- **Request**: Multipart form data.
- **Response**:
  ```json
  {
    "filename": "uploaded_image.jpg"
  }
  ```

---

## **🎨 UI Screenshots**

### **Homepage**:
Displays a list of all blog posts.
![Homepage Screenshot](https://github.com/Adebowale-Morakinyo/blog-website-project/blob/main/frontend/public/images/home_page.png)

### **Post View**:
Shows the content of a selected blog post.
![Post View Screenshot](https://github.com/Adebowale-Morakinyo/blog-website-project/blob/main/frontend/public/images/individual_post.png)

### **Post Editor**:
Allows users to create a new blog post.
![Post Editor Screenshot](https://github.com/Adebowale-Morakinyo/blog-website-project/blob/main/frontend/public/images/post_editor.png)

---

## **📦 Installation and Setup**

### **Backend**:
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd blog-website-project/backend
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

### **Frontend**:
1. Navigate to the `frontend` directory:
   ```bash
   cd ../frontend
   ```
2. Open `index.html` in your browser (or use Live Server for a better experience).

---

## **🌟 Future Features**

- 🔍 **Search by Tags**: Filter blog posts by tags.
- 💬 **Comments Section**: Allow users to leave comments on posts.
- 🔐 **User Authentication**: Enable user login to manage their posts.
- 📅 **Post Scheduling**: Schedule posts to be published at a later date.

---

## **🤝 Contributing**

We welcome contributions from everyone! If you’d like to improve this project, feel free to fork the repository, make changes, and submit a pull request.

---

## **📜 License**

This project is licensed under the  GPL-3.0 license.

---

## **✨ Acknowledgements**

- Icons and design inspiration from Astro.
- Frameworks and libraries: FastAPI, Bootstrap, SQLite.

---
