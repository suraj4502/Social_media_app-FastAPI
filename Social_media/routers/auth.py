from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from Social_media import models, schemas, utils, oauth2
from Social_media.database import get_db

router = APIRouter(tags=['Authentication'])

@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    print("Credentials For Login ::", user_credentials.username, user_credentials.password)
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user or not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Here you would generate a token and return it
    access_token = oauth2.create_access_tokens(data = {"user_id" : user.id})  
    
    return {"access_token": access_token, "token_type": "bearer"}
