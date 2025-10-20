"""
OCR Wrapper module using PaddleOCR.
"""
from paddleocr import PaddleOCR
import numpy as np
import cv2

# Initialize OCR model (can be parameterized for v3/v5/TrOCR)
ocr_model = PaddleOCR(use_angle_cls=True, lang='en')

def run_ocr(image_bytes):
    # Decode image bytes
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Run OCR
    result = ocr_model.ocr(img, cls=True)
    # Parse text results
    lines = []
    for line in result[0]:
        text = line[1][0]
        lines.append(text)
    return lines
