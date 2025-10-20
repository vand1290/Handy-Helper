"""
Watch a folder for new images and trigger OCR processing.
"""
import time
import os

WATCH_PATH = "./watched_folder"

def process_file(filepath):
    print(f"Processing: {filepath}")
    # TODO: call OCR API or directly invoke run_ocr

def watch_folder(path):
    seen = set()
    while True:
        files = set(os.listdir(path))
        new_files = files - seen
        for fname in new_files:
            if fname.lower().endswith(('.png', '.jpg', '.jpeg')):
                process_file(os.path.join(path, fname))
        seen = files
        time.sleep(2)

if __name__ == "__main__":
    if not os.path.exists(WATCH_PATH):
        os.makedirs(WATCH_PATH)
    watch_folder(WATCH_PATH)