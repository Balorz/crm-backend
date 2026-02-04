from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, Token
from app.services.auth_service import create_user, authenticate_user, create_user_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup", response_model=Token)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    """Register a new user and return JWT token."""
    user = create_user(db, user_data)
    return create_user_token(user)


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login with email and password, return JWT token."""
    from app.schemas.user import UserLogin
    user_login = UserLogin(email=form_data.username, password=form_data.password)
    user = authenticate_user(db, user_login)
    return create_user_token(user)
