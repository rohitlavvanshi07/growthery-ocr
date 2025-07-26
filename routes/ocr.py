from fastapi import APIRouter, UploadFile, File, HTTPException
from utils.ocr_processor import extract_text_from_image

router = APIRouter()

@router.post("/extract")
async def extract_text(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
    
    content = await file.read()
    text = extract_text_from_image(content)
    return {"text": text}
