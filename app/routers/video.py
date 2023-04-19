from fastapi import FastAPI,Request, APIRouter, UploadFile,File,Form,HTTPException
from fastapi.responses import HTMLResponse,FileResponse
from services import stream_service

router = APIRouter()
  

@router.post("/upload",response_class=HTMLResponse)
async def upload_video(request: Request, file: UploadFile=File(...)):
    return stream_service.uploadVideo(request,file)

@router.post("/download",response_class=FileResponse)
async def download_video(request: Request,filename: str =Form(...)):
    return stream_service.downloadVideo(request,filename)

@router.post("/stream")
async def stream_video(request: Request,filename: str = Form(...)):
    return stream_service.streamVideo(request,filename)
