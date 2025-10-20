# Handwriting OCR Starter

A desktop (FastAPI-based) app for scanning handwritten images and extracting structured data using OCR.

## Features
- FastAPI endpoints for OCR and structured field extraction
- PaddleOCR backend (v3/v5/TrOCR support planned)
- Optional batch/folder watcher for automation
- ONNX quantization tool

## Project Structure

```
app/
  main.py          # FastAPI app (API endpoints)
  extractor.py     # Field extractors for structured data
  ocr.py           # OCR wrapper using PaddleOCR
  models.py        # Model loading logic (v3/v5/TrOCR)
requirements.txt
README.md
tools/
  watch_folder.py  # Batch/folder watcher
  quantize_onnx.py # Optional ONNX quantization script
```

## Quickstart

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the FastAPI app:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Send a POST request to `/ocr/` with an image file.

## License

MIT