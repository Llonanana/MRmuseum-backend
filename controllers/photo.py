from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.email import send_group_photo

photo_router = APIRouter(prefix='/photo', tags=['photo'])

class GroupPhotoEmail(BaseModel):
    email: str
    photo_base64: str
    file_name: str

@photo_router.post('/email')
def send_group_photo_controller(payload: GroupPhotoEmail):
    try:
        send_group_photo(payload.email, payload.photo_base64, payload.file_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": "sent"}
