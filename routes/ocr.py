from fastapi import APIRouter, UploadFile, File, HTTPException
from utils.ocr_processor import extract_text_from_pdf

router = APIRouter()

@router.post("/extract")
async def extract_text(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF.")
    
    content = await file.read()
    text = extract_text_from_pdf(content)
    return {"text": text}
