"""
Model loader for OCR (v3/v5/TrOCR support placeholder).
Extend to allow dynamic model selection/loading.
"""
def load_model(model_type="paddleocr_v3"):
    if model_type == "paddleocr_v3":
        # Placeholder: import and instantiate PaddleOCR v3
        pass
    elif model_type == "paddleocr_v5":
        # Placeholder: PaddleOCR v5
        pass
    elif model_type == "trocr":
        # Placeholder: TrOCR model loading
        pass
    else:
        raise ValueError(f"Unknown model type: {model_type}")