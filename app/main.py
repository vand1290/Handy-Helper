"""
FastAPI entry point for the OCR Desktop App.
Provides API endpoints for image upload and OCR processing.
"""
from fastapi import FastAPI, UploadFile, File
from app.ocr import run_ocr
from app.extractor import extract_fields

app = FastAPI(title="Handwriting OCR Starter")

@app.post("/ocr/")
async def ocr_endpoint(file: UploadFile = File(...)):
    # Read file contents
    image_bytes = await file.read()
    # Run OCR
    ocr_result = run_ocr(image_bytes)
    # Extract structured fields (optional)
    extracted = extract_fields(ocr_result)
    return {"ocr": ocr_result, "extracted": extracted}