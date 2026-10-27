from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.status import HTTP_404_NOT_FOUND

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
posts:list[dict] = [
    {
        "id":1,
        "author":"Waqar Ahmad",
        "title":"FastAPI for backend develompment",
        "content":"FastAPI is awesome for API development..",
        "date_posted":"09-oct-2021"
    },
   {
        "id":2,
        "author":"Bilal Ahmad",
        "title":"Python Programming is good for AI",
        "content":"Python for AI is the best programming language",
        "date_posted":"09-oct-2021"
    },
]

@app.get('/posts/view')
@app.get('/posts', include_in_schema=False)
def get_data(request:Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts":posts, "title":"Home"}
    )


@app.get("/posts/api/{blog_id}")
def get_post(blog_id:int):
    for post in posts:
        if post.get("id") == blog_id:
            return post
        
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Post not Found")

@app.get("/about")
def about(request:Request):
    return templates.TemplateResponse(request, "about.html", {"title":"About"})

@app.get('/')
def home():
    return {"message: Hello World"}