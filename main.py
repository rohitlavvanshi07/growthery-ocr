from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ocr import router as ocr_router

app = FastAPI()

# CORS setup (safe to allow all for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "OCR service is live!"}

# Mount the OCR router
app.include_router(ocr_router, prefix="/ocr")
