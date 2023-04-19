from fastapi import FastAPI,Request, APIRouter, UploadFile,File
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
import shutil

router = APIRouter()
templates = Jinja2Templates("static/templates/")

def save_upload_file(upload_file: UploadFile, destination: str) -> None:
    try:
        with open(destination,"wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()

def uploadVideo(request: Request,file: UploadFile):
    
    if file == None:
        return templates.TemplateResponse("index.html",{"request":request})
    if file.filename=='':
        return templates.TemplateResponse("index.html",{"request":request})
    else:
        path = 'static/videos/'+ file.filename
        
        save_upload_file(file, path)
		#print('upload_video filename: ' + filename)
        return templates.TemplateResponse('index.html', {"request":request, "filename":file.filename})


@router.post("/upload")
async def upload_video(request: Request, file: UploadFile=File(...)):
    return uploadVideo(request,file)
