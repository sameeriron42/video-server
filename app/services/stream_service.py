from fastapi import Request,  UploadFile
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import shutil,os


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
        msg = "Video with the name "+ file.filename+" is uploaded"
        return templates.TemplateResponse('index.html', {"request":request, "response_msg":msg})

def downloadVideo(request: Request,file_name: str):
    file_location= 'static/videos/'+file_name
    if os.path.isfile(file_location)== False:
        return templates.TemplateResponse("index.html",{"request":request, "response_msg":"The video with the given name does not exist"})

    return FileResponse(path=file_location,media_type='video/mp4',filename=file_name)

def streamVideo(request:Request,file_name: str):
    file_location= 'static/videos/'+file_name
    if os.path.isfile(file_location)== False:
        return templates.TemplateResponse("index.html",{"request":request, "response_msg":"The video with the given name does not exist"})

    return templates.TemplateResponse('index.html', {"request":request, "filename": file_name})
 