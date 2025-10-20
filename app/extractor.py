"""
Field extractor functions to structure OCR results.
Implement custom logic as needed.
"""
def extract_fields(ocr_lines):
    # Example: find date or amount fields (customize as needed)
    fields = {}
    for line in ocr_lines:
        if "date" in line.lower():
            fields["date"] = line
        if "amount" in line.lower():
            fields["amount"] = line
    return fields
