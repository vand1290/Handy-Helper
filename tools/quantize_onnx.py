"""
Script to quantize an ONNX OCR model for faster inference.
"""
import onnx
from onnxruntime.quantization import quantize_dynamic, QuantType

def quantize(model_fp, quantized_fp):
    quantize_dynamic(
        model_fp, quantized_fp,
        weight_type=QuantType.QInt8
    )
    print(f"Quantized model saved to {quantized_fp}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python quantize_onnx.py <model.onnx> <quantized.onnx>")
    else:
        quantize(sys.argv[1], sys.argv[2])