from fastapi import APIRouter
from core.firebase import db
from core.config import config
from schemas.user import User

router = APIRouter()


@router.post('/')
def create_user(user: User):
    try:
        uid = str(user.id)
        doc_ref = db.collection(config.USER_TABLE_STR).document(uid)
        user_ref = doc_ref.get()

        if user_ref.exists:
            return {'status': 'error', 'message': 'User already exists'}

        doc_ref.set(user.to_json())
        return {'status': 'success', 'data': user}
    except:
        return {'status': 'error', 'message': 'An exception occurred'}


@router.get('/')
def read_users(limit: str = 10):
    try:
        users_ref = db.collection(config.USER_TABLE_STR).limit(limit)
        data = users_ref.stream()

        return {'status': 'success', 'data': data}
    except:
        return {'status': 'error', 'message': 'An exception occurred'}
