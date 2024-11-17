from sqlalchemy.orm import Session
from . import models, schemas

# Create a blog post
from sqlalchemy.exc import SQLAlchemyError

def create_blog(db: Session, blog: schemas.BlogCreate):
    try:
        print(f"Attempting to create blog: {blog.title}")  # Debug message
        db_blog = models.BlogPost(
            title=blog.title,
            content=blog.content,
            image_url=blog.image_url,
            tags=blog.tags
        )
        db.add(db_blog)
        db.commit()
        db.refresh(db_blog)
        print(f"Successfully created blog with ID: {db_blog.id}")  # Debug message
        return db_blog
    except SQLAlchemyError as e:
        print(f"Error creating blog: {str(e)}")  # Log the error for debugging
        db.rollback()  # Rollback the transaction to maintain database integrity
        raise


# Get a list of blog posts
def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.BlogPost).offset(skip).limit(limit).all()

# Get a single blog post
def get_blog(db: Session, blog_id: int):
    return db.query(models.BlogPost).filter(models.BlogPost.id == blog_id).first()

# Update a blog post
def update_blog(db: Session, blog_id: int, blog: schemas.BlogUpdate):
    db_blog = get_blog(db, blog_id)
    if db_blog:
        db_blog.title = blog.title
        db_blog.content = blog.content
        db_blog.image_url = blog.image_url
        db.commit()
        db.refresh(db_blog)
    return db_blog

# Delete a blog post
def delete_blog(db: Session, blog_id: int):
    db_blog = get_blog(db, blog_id)
    if db_blog:
        db.delete(db_blog)
        db.commit()
    return db_blog
