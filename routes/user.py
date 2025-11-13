from fastapi import APIRouter
from schemas.user import (FullUserProfile, 
                          MultipleUsersResponse, 
                          createUserResponse
)


from services.user import UserService

def create_user_router() -> APIRouter:
    user_router = APIRouter(
        prefix="/user_endpoint",
        tags =["user"]
    )
    user_service = UserService()
    
    
    @user_router.get("/all", response_model=MultipleUsersResponse)
    def get_all_users_paginated(start: int = 0, limit: int = 2):
        users, total = user_service.get_all_users_with_pagination(start, limit)
        formatted_users = MultipleUsersResponse(users=users, total=total)
        return formatted_users


    @user_router.get("/{user_id}", response_model=FullUserProfile)
    def get_user_by_id(user_id: int):
        """
        Endpoint for retrieving a FullUserProfile by the user's unique indentifier
        :param user_id: unique monotomically increasing integer id
        :return: 
        """
        full_user_profile = user_service.getUserInfo(user_id)
        return full_user_profile

    @user_router.put("/user_id")
    def update_user(user_id: int, full_profile_info: FullUserProfile):
        user_service.create_update_user(full_profile_info, user_id)
        return None

    @user_router.delete("/user_id")
    def remove_user(user_id, int):
        user_service.delete_user(user_id)


    @user_router.post("/", response_model=createUserResponse)
    def add_user(full_profile_info: FullUserProfile):
        user_id = user_service.create_update_user(full_profile_info)
        print("doc string of create_update_user:\n", user_service.create_update_user.__doc__)
        created_user = createUserResponse(user_id=user_id)
        return created_user
    return user_router