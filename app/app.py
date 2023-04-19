from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers import video

app = FastAPI()
app.mount(path="/static",app=StaticFiles(directory="static"),name="static")
templates = Jinja2Templates("static/templates/")
app.include_router(video.router)

@app.get("/",response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html",context={"request": request})