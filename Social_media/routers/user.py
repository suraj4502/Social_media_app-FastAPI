from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix= "/users",
    tags= ['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED , response_model = schemas.UserOut)
def create_posts(user: schemas.UserCreate , db: Session = Depends(get_db)):
    try:
        hashed_password = utils.hash(user.password)
        user.password = hashed_password
        new_user = models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/{id}", response_model= schemas.UserOut)
def get_post(id :int, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                                detail= f"post with id={id} was not found.")
        return user
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    