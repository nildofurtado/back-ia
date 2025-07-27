from datetime import datetime
from zoneinfo import ZoneInfo
from app.models.user_model import UserCreate, UserUpdate, UserModel
from app.database.mongodb import user_collection
from app.utils.password import hash_password
from bson import ObjectId


async def create_user(user: UserCreate):
    user_dict = user.dict()
    user_dict["created"] = datetime.now(ZoneInfo("America/Sao_Paulo"))
    user_dict["password"] = hash_password(user.password)
    result = await user_collection.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return UserModel(**user_dict)


async def update_user(user_id: str, data: UserUpdate):
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])

    result = await user_collection.update_one(
        {"_id": ObjectId(user_id)}, {"$set": update_data}
    )
    if result.matched_count == 0:
        return None
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    return UserModel(**user)


async def delete_user(user_id: str):
    result = await user_collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count == 1


async def get_user_by_email(email: str):
    user = await user_collection.find_one({"email": email})
    if not user:
        return None

    user["_id"] = str(user["_id"])
    return UserModel(**user)
