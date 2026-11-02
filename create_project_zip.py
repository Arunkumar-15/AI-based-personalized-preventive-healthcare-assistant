"""
Bundles 100% of all implemented frontend code, backend code, trained ML models,
datasets, and PDF documentation into AI_Healthcare_Assistant_Project.zip.
"""

import os
import zipfile
import shutil

def zip_project():
    root_dir = r"C:\Users\arunk\Projects\health-assistant"
    output_zip_proj = r"C:\Users\arunk\Projects\AI_Healthcare_Assistant_Project.zip"
    output_zip_down = r"C:\Users\arunk\Downloads\AI_Healthcare_Assistant_Project.zip"

    # Exclude heavy temporary directories
    exclude_dirs = {'.venv', 'node_modules', '.git', 'dist', '__pycache__', '.pytest_cache'}

    file_count = 0
    with zipfile.ZipFile(output_zip_proj, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(root_dir):
            # Modify dirs in-place to skip excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                if file.endswith('.zip') or file.endswith('.pyc'):
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, root_dir)
                zipf.write(file_path, arcname)
                file_count += 1

        # Also copy generated PDFs from Downloads into the root of the ZIP if present
        pdf_files = [
            r"C:\Users\arunk\Downloads\AI_Healthcare_Assistant_Implementation_Plan.pdf",
            r"C:\Users\arunk\Downloads\AI_Healthcare_Assistant_System_Workflow.pdf",
            r"C:\Users\arunk\Downloads\AI_Healthcare_Assistant_Complete_Project_Conversation_History.pdf",
            r"C:\Users\arunk\Downloads\AI_Healthcare_Assistant_Complete_Project_Conversation_History.md",
            r"C:\Users\arunk\Downloads\Sample_Medical_Lab_Report.pdf",
            r"C:\Users\arunk\Downloads\healthcare_clinical_biomarkers_mode2.csv",
            r"C:\Users\arunk\Downloads\medical_ocr_extracted_reports_mode3.csv"
        ]

        for pdf in pdf_files:
            if os.path.exists(pdf):
                fname = os.path.basename(pdf)
                zipf.write(pdf, os.path.join("documentation_and_datasets", fname))
                file_count += 1

    shutil.copy2(output_zip_proj, output_zip_down)
    print(f"Successfully packaged {file_count} files into {output_zip_down}")

if __name__ == '__main__':
    zip_project()
