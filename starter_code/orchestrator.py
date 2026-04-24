import os
import json
import glob

# Import các thành phần từ các module liên quan
# Lưu ý: Đảm bảo các file schema.py, process_unstructured.py, quality_check.py nằm cùng thư mục hoặc trong PYTHONPATH
from process_unstructured import process_pdf_data, process_video_data
from quality_check import run_semantic_checks

# ==========================================
# ROLE 4: DEVOPS & INTEGRATION SPECIALIST
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_DIR = os.path.join(BASE_DIR, "..", "raw_data")
OUTPUT_FILE = os.path.join(BASE_DIR, "..", "processed_knowledge_base.json")

def run_pipeline():
    final_kb = []
    
    # --- Xử lý Group A (PDFs) ---
    pdf_files = glob.glob(os.path.join(RAW_DATA_DIR, "group_a_pdfs", "*.json"))
    print(f"Found {len(pdf_files)} PDF raw files.")
    
    for file_path in pdf_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            
            # Bước 1: Gọi hàm xử lý PDF
            processed_doc = process_pdf_data(raw_data)
            
            # Bước 2: Kiểm tra chất lượng (Semantic Checks)
            if run_semantic_checks(processed_doc):
                final_kb.append(processed_doc)
            else:
                print(f"Skipped PDF file {file_path} due to failed quality checks.")
                
        except Exception as e:
            print(f"Error processing PDF {file_path}: {e}")

    # --- Xử lý Group B (Videos) ---
    video_files = glob.glob(os.path.join(RAW_DATA_DIR, "group_b_videos", "*.json"))
    print(f"Found {len(video_files)} Video raw files.")
    
    for file_path in video_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            
            # Bước 1: Gọi hàm xử lý Video
            processed_doc = process_video_data(raw_data)
            
            # Bước 2: Kiểm tra chất lượng
            if run_semantic_checks(processed_doc):
                final_kb.append(processed_doc)
            else:
                print(f"Skipped Video file {file_path} due to failed quality checks.")
                
        except Exception as e:
            print(f"Error processing Video {file_path}: {e}")

    # --- Lưu kết quả ---
    # Đảm bảo thư mục đầu ra tồn tại
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_kb, f, indent=4, ensure_ascii=False)
        
    print("-" * 30)
    print(f"Pipeline finished!")
    print(f"Total processed and validated records: {len(final_kb)}")
    print(f"Result saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    run_pipeline()