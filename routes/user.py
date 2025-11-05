from fastapi import APIRouter

user_router = APIRouter


@user_router.get("/user/me", response_model=FullUserProfile)
def test_endpoint():
    full_user_profile = getUserInfo()
    return full_user_profile


@user_router.get("/user/{user_id}", response_model=FullUserProfile)
def get_user_by_id(user_id: int):
    """
    Endpoint for retrieving a FullUserProfile by the user's unique indentifier
    :param user_id: unique monotomically increasing integer id
    :return: 
    """
    full_user_profile = getUserInfo(user_id)
    return full_user_profile



@user_router.put("/user/user_id")
def update_user(user_id: int, full_profile_info: FullUserProfile):
    create_update_user(full_profile_info, user_id)
    return None

@user_router.delete("/user/user_id")
def remove_user(user_id, int):
    delete_user(user_id)


@user_router.get("/user", response_model=MultipleUsersResponse)
def get_all_users_paginated(start: int = 0, limit: int = 2):
    users, total = get_all_users_with_pagination(start, limit)
    formatted_users = MultipleUsersResponse(users=users, total=total)
    return formatted_users


@user_router.post("/users", response_model=createUserResponse)
def add_user(full_profile_info: FullUserProfile):
    user_id = create_update_user(full_profile_info)
    print("doc string of create_update_user:\n", create_update_user.__doc__)
    created_user = createUserResponse(user_id=user_id)
    return created_user