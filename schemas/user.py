from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):  
    username: Optional[str] = Field(
        alias="name",
        title="The Username",
        description="Username of the user",
        min_length=1,
        default=None
    )
    likedPosts: list[int] =Field(
        alias="liked_posts",
        description="Array of post ids the user liked",
        default_factory=list
    )
    
class FullUserProfile(User):
    short_description: str
    long_bio: str
    

class MultipleUsersResponse(BaseModel):
    users: list[FullUserProfile] 
    total:int
    
    
class createUserResponse(BaseModel):
    user_id: int
    
    