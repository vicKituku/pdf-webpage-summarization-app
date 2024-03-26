from fastapi import FastAPI, Request, Form, File, UploadFile
from langchain_community.document_loaders import PyPDFLoader
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from url_summarizer import url_summarizer
from pdf_summarizer import pdf_summarizer
from io import BytesIO
import os


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")
UPLOAD_DIR = 'uploads'


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.post('/')
async def url_summary(request: Request, url: str = Form(...)):
    summary  = url_summarizer(url)
    print(f'summary: {summary}')
    
    return templates.TemplateResponse("index.html", {'request': request, 'summary': summary})

@app.get("/pdf-summary")
async def home(request: Request):
    return templates.TemplateResponse("pdf.html", {"request":request})

@app.post("/pdf-summary")
async def pdf_summary(request: Request, file: UploadFile = File(...)):
    content = await file.read()
    # Save the uploaded file locally
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    print(file_path)
    with open(file_path, "wb") as f:
        f.write(content)
    summary = pdf_summarizer(file_path)
    return templates.TemplateResponse("pdf.html", {'request': request, 'summary': summary})