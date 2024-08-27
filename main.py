from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

#decorator
@app.get("/")
def root():
    return {"Hello": "Welcome to my api endpoint"}

@app.get("/posts")
def get_posts():
    return {"data": "blog list"}
#payload
@app.post("/createposts")
def create_posts(payload: dict=Body(...)):
    print(payload)
    return {"new_post": f"post created with title {payload['title']} content is {payload['content']}"}

