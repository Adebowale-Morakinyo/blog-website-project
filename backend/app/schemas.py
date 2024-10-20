from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base schema for Blog
class BlogBase(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
    tags: Optional[str] = None  # Tags as a comma-separated string

# Schema for creating a new blog
class BlogCreate(BlogBase):
    pass

# Schema for updating an existing blog
class BlogUpdate(BlogBase):
    pass

# Schema for the response
class Blog(BlogBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
