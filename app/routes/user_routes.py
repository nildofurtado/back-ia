from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer
from app.models.user_model import UserCreate, UserUpdate, UserModel
from app.services.user_service import create_user, update_user, delete_user, get_user_by_email
from app.services.email_service import EmailService

bearer_scheme = HTTPBearer()
router = APIRouter(prefix="/users", tags=["Usuários"])


@router.get("/{email}", response_model=UserModel, dependencies=[Depends(bearer_scheme)])
async def get_user(email: str):
    data = await get_user_by_email(email)
    if not data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return data

@router.post("/", response_model=UserModel, dependencies=[Depends(bearer_scheme)])
async def create(user: UserCreate):
    existing = await get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    return await create_user(user)

@router.put("/{user_id}", response_model=UserModel, dependencies=[Depends(bearer_scheme)])
async def update(user_id: str, user: UserUpdate):
    updated = await update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return updated

@router.delete("/{user_id}", dependencies=[Depends(bearer_scheme)])
async def delete(user_id: str):
    success = await delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return {"detail": "Usuário removido com sucesso."}

@router.post("/reset-password", dependencies=[Depends(bearer_scheme)])
async def reset_password(email: str):
    user = await get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="Email não encontrado.")
   
    token = "token-simulacao"  # ideal: JWT ou UUID + TTL
    EmailService().send_password_reset(email, token)
    return {"detail": "Email de redefinição enviado com sucesso."}

