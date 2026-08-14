from pathlib import Path
UPLOAD=Path(__file__).resolve().parent.parent/"data"/"uploads";UPLOAD.mkdir(parents=True,exist_ok=True)
def save_upload(filename,data):
    p=UPLOAD/Path(filename).name;p.write_bytes(data);return p
def read_file_text(name):
    p=UPLOAD/Path(name).name
    if p.suffix.lower() in {".txt",".md",".py",".js",".html",".css",".json",".csv"}:return p.read_text(encoding="utf-8",errors="ignore")
    if p.suffix.lower()==".pdf":
        try:
            from pypdf import PdfReader
            return "\n".join(page.extract_text() or "" for page in PdfReader(str(p)).pages)
        except:return "PDF extraction unavailable."
    return "Unsupported text format."
