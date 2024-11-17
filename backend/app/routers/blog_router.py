from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from .. import crud, schemas, database
import shutil
from pathlib import Path
from datetime import datetime


router = APIRouter(
    prefix="/blogs",
    tags=["blogs"]
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new blog
@router.post("/", response_model=schemas.Blog)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    try:
        print(f"Received request to create blog: {blog.title}")  # Debug message
        created_blog = crud.create_blog(db, blog)
        print(f"Blog created successfully with ID: {created_blog.id}")  # Debug message
        return created_blog
    except Exception as e:
        print(f"Error in create_blog endpoint: {str(e)}")  # Log the error for debugging
        raise HTTPException(status_code=500, detail="An error occurred while creating the blog post")

# Get list of blogs
@router.get("/", response_model=list[schemas.Blog])
def read_blogs(skip: int = 0, limit: int = 40, db: Session = Depends(get_db)):
    return crud.get_blogs(db, skip=skip, limit=limit)

# Get a single blog
@router.get("/{blog_id}", response_model=schemas.Blog)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.get_blog(db, blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog

# Update a blog
@router.put("/{blog_id}", response_model=schemas.Blog)
def update_blog(blog_id: int, blog: schemas.BlogUpdate, db: Session = Depends(get_db)):
    return crud.update_blog(db, blog_id, blog)

# Delete a blog
@router.delete("/{blog_id}", response_model=schemas.Blog)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    return crud.delete_blog(db, blog_id)

# Add this to your router file
@router.post("/upload-image/", response_model=schemas.ImageUploadResponse)
async def upload_image(image: UploadFile = File(...)):
    try:
        # Define the path to save the image
        UPLOAD_DIR = Path("../frontend/public/images")
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        
        # Generate unique filename using timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{timestamp}-{image.filename}"
        
        # Save the file
        file_path = UPLOAD_DIR / filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        
        # Optional URL generation, modify as needed
        # image_url = f"/images/{filename}"
        # Return response
        return schemas.ImageUploadResponse(filename=filename)
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))