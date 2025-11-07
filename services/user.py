from typing import Optional
from schemas.user import FullUserProfile, User


profile_infos = {
    0: {
        "short_description": "My bio description", 
        "long_bio": "Extended info"
    }
}


users_content = {
    0: {
        "liked_posts": [1]*9,
    }
}

class UserService:
    def __init__(self):
        pass

    def get_all_users_with_pagination(self, start: int, limit: int) -> tuple[list[FullUserProfile], int]:
        list_of_users = []
        keys = list(profile_infos.keys())
        total = len(keys)
        
        for index in range(0, len(keys), 1):
            if index < start:
                continue
            current_key = keys[index]
            user = self.getUserInfo(current_key)
            list_of_users.append(user)
            if len(list_of_users) >= limit:
                break
            
        return list_of_users , total
    
    @staticmethod
    def getUserInfo(user_id: int = 0) -> FullUserProfile:
        profile_info = profile_infos[user_id]
        
        user_content = users_content[user_id]
        
        user = User(**user_content)
        
        full_user_profile = {
            **profile_info,
            **user.dict()
        }
         
        return FullUserProfile(**full_user_profile)  

    @staticmethod    
    def create_update_user(full_profile_info: FullUserProfile, new_user_id: Optional[int] = None) -> int:
        """
        Create user and new unique user id if not exist other update user
        placeholder implementation to be later updated to db
        :param full_profile_info: ullUserProfile - User info saved in db
        :param new_user_id Optional(int) - user_id if already exists, Otherwise to be set
        :return:
        
        """
        global profile_infos
        global users_content
        
        if new_user_id is None:
            new_user_id = len(profile_infos)
        
        liked_posts = full_profile_info.likedPosts
        short_description = full_profile_info.short_description
        long_bio = full_profile_info.long_bio
        
        print("before:")
        print("users_content", users_content)
        print("profile_infos", profile_infos)
        
        users_content[new_user_id] = {"likedPosts": liked_posts}
        profile_infos[new_user_id] = {
            "short_description": short_description,
            "longBio": long_bio
        }
        print("after:")
        print("users_content", users_content)
        print("profile_infos", profile_infos)
        
        return new_user_id
    @staticmethod
    def delete_user(user_id:int) -> None:
        global profile_infos
        global users_content
        
        del profile_infos[user_id]
        del users_content[user_id]