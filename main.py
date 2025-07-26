from fastapi import FastAPI, UploadFile, File
from PyPDF2 import PdfReader
import io

app = FastAPI()

@app.post("/extract-pdf-buffer")
async def extract_pdf_buffer(file: UploadFile = File(...)):
    contents = await file.read()
    reader = PdfReader(io.BytesIO(contents))
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    
    return {"text": text.strip()}
