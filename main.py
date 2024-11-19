from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

my_posts = [{"title": "Post 1", "content": "This is my first post", "id": 1},
            {"title": "Post 2", "content": "This is my second post", "id": 2}]

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
    return {"data": my_posts}


#payload
@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0,100000000)
    my_posts.append(post_dict)
    return {"data": post_dict} 

