from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional[int] = None

#decorator
@app.get("/")
def root():
    return {"Hello": "Welcome to my api endpoint"}

@app.get("/posts")
def get_posts():
    return {"data": "blog list"}
#payload
@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.title)
    print(new_post.content)
    print(new_post.published)
    print(new_post.rating)
    return {"data": "new post"} 

