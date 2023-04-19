# video-server
webserver written in fastAPI to upload, download and stream videos
## Run Locally

Clone the project

```bash
  git clone https://github.com/sameeriron42/video-server.git
```

Go to the project directory

```bash
  cd video-server
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Set PYTHONPATH environment variable for modules imports

**For UNIX (Linux, OSX, ...)**
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"
```
**For Windows**
```bash
set PYTHONPATH=%PYTHONPATH%;C:\path\to\your\project\
 ```
Start FastAPI server
```bash
  cd app/
  uvicorn app:app --reload
```
