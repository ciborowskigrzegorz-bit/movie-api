from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/movies/", response_model=list[schemas.Movie])
def read_movies(db: Session = Depends(get_db)):
    return crud.get_movies(db)

@router.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id)
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.post("/movies/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@router.delete("/movies/{movie_id}", response_model=schemas.Movie)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    return crud.delete_movie(db, movie_id)
