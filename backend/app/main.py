from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import blog_router
from .database import Base, engine

# Initialize the database
Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI()

# CORS configuration
origins = [
    "http://127.0.0.1:5500",  # Your frontend's origin (for development)
    "http://localhost:5500",  # Localhost as well
    # You can add production origins here once deployed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # Allow requests from these origins
    allow_credentials=True,
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],     # Allow all headers
)

# Include routers
app.include_router(blog_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog API!"}
