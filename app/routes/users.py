from fastapi import APIRouter, Depends

from app.models.users import UserCreate, UserUpdate
from app.service.users import UserService
from app.dal.user import UserDAL
router = APIRouter()

def get_user_service():
    return UserService(UserDAL())

@router.get("/", response_model=None)
async def get_users(user_service: UserService = Depends(get_user_service)):
    return await user_service.get_users()

@router.get("/{id}", response_model=None)
async def get_user(id: int, user_service: UserService = Depends(get_user_service)):
    return await user_service.get_user(id)

@router.post("/", response_model=None)
async def create_users(request: UserCreate, user_service: UserService = Depends(get_user_service)):
    return await user_service.create_user(request.model_dump())

@router.patch("/{id}", response_model=None)
async def update_users(id: int, user: UserUpdate, user_service: UserService = Depends(get_user_service)):
    return await user_service.update_user(id, user.model_dump())