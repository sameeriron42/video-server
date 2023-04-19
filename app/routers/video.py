from fastapi import FastAPI,Request, APIRouter, UploadFile,File,Form,HTTPException
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
import shutil,os

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
        return templates.TemplateResponse("index.html",{"request":request, "response_msg":"please upload first"})
    if file.filename=='':
        return templates.TemplateResponse("index.html",{"request":request, "response_msg":"please upload first"})
    if file.content_type !='video/mp4':
        return templates.TemplateResponse("index.html",{"request":request, "response_msg":"Only Video/Mp4 supported"})
    else:
        path = 'static/videos/'+ file.filename
        
        save_upload_file(file, path)
        return templates.TemplateResponse('index.html', {"request":request, "filename":file.filename})

def downloadVideo(request: Request,file_name: str):
    file_location= 'static/videos/'+file_name
    if os.path.isfile(file_location)== False:
        return templates.TemplateResponse("index.html",{"request":request, "response_msg":"The video with the given name does not exist"})

    return FileResponse(path=file_location,media_type='video/mp4',filename=file_name)


@router.post("/upload",response_class=HTMLResponse)
async def upload_video(request: Request, file: UploadFile=File(...)):
    return uploadVideo(request,file)

@router.post("/download",response_class=FileResponse)
async def download_video(request: Request,filename: str =Form(...)):
    return downloadVideo(request,filename)

