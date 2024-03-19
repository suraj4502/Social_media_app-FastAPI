from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import select, func
from sqlalchemy.orm import aliased

from Social_media import models, schemas, oauth2
from Social_media.database import get_db


router = APIRouter(
    prefix= "/posts",
    tags= ['Posts']
)



@router.get("/", response_model= List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user), 
              limit : int = 10, skip : int = 0, search : Optional[str] = ''):
    stmt = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
                            models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id)
    results = stmt.filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    print("QUERY ::", stmt)
    # print("Results ::", results)
    return results


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.PostReponse)
def create_posts(post: schemas.CreatePost , db: Session = Depends(get_db), 
                 current_user : int = Depends(oauth2.get_current_user)):
    try:
        print('current_user ::' , current_user.email, current_user.id)
        new_post = models.Post(owner_id = current_user.id, **post.model_dump())
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   

@router.get("/{id}", response_model= schemas.PostOut,)
def get_post(id :int, db: Session = Depends(get_db),
             current_user : int = Depends(oauth2.get_current_user)):
    try:
        post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
                        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
                            models.Post.id).filter(models.Post.id == id).first()
        if not post:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                                detail= f"post with id={id} was not found.")
        return post
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def get_post(id :int, db: Session = Depends(get_db),
             current_user : int = Depends(oauth2.get_current_user)):
    try:
        del_query = db.query(models.Post).filter(models.Post.id == id)
        
        if del_query.first() == None:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                                detail= f"post with id={id} was not found.")
        if del_query.first().owner_id == current_user.id:
            del_query.delete(synchronize_session= False)
            db.commit()
            return Response(status_code= status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail = f"Not authorized to perform the requested Action.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model= schemas.PostReponse)
def create_posts(id: int, post : schemas.CreatePost, db: Session = Depends(get_db),
                 current_user : int = Depends(oauth2.get_current_user)):
    try:
        update_query = db.query(models.Post).filter(models.Post.id == id)
        udpated_post = update_query.first()
        if not udpated_post:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                                detail= f"post with id={id} was not found.")    
        if udpated_post.owner_id == current_user.id: 
            update_query.update(post.model_dump(), synchronize_session=False)
            db.commit()
            return  update_query.first()
        else:
            raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail = f"Not authorized to perform the requested Action.")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))