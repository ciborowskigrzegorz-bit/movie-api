from pydantic import BaseModel, ConfigDict

class MovieBase(BaseModel):
    title: str
    director: str
    year: int

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
