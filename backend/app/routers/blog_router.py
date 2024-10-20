from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

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
    return crud.create_blog(db, blog)

# Get list of blogs
@router.get("/", response_model=list[schemas.Blog])
def read_blogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
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
