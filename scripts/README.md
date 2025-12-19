# Document Processing Scripts

Utilities for converting various document formats to Markdown for use in Claude Project knowledge bases.

## Scripts

| Script | Input | Description |
|--------|-------|-------------|
| `pptx_to_markdown.py` | `.pptx` | Converts PowerPoint presentations. Preserves slides, titles, speaker notes, and tables. |
| `xlsx_to_markdown.py` | `.xlsx`, `.xls` | Converts Excel spreadsheets to Markdown tables. Handles multiple sheets. |
| `pdf_ocr_to_markdown.py` | `.pdf` | Converts PDFs to Markdown. Uses OCR for scanned/image-based documents. |

## Usage

**Single file:**
```bash
python pptx_to_markdown.py input.pptx [output.md]
python xlsx_to_markdown.py input.xlsx [output.md]
python pdf_ocr_to_markdown.py input.pdf [output.md]
```

**Batch conversion (all files in folder):**
```bash
python pptx_to_markdown.py /path/to/folder
python xlsx_to_markdown.py /path/to/folder
python pdf_ocr_to_markdown.py /path/to/folder
```

## Dependencies

```bash
# PowerPoint
pip install python-pptx

# Excel
pip install openpyxl

# PDF with OCR
pip install pymupdf pytesseract Pillow
```

For PDF OCR, Tesseract must also be installed:
- **Windows**: [UB-Mannheim installer](https://github.com/UB-Mannheim/tesseract/wiki)
- **Mac**: `brew install tesseract`
- **Linux**: `sudo apt-get install tesseract-ocr`

## Notes

- Claude can read PDFs and Word docs natively - these scripts are for formats that benefit from Markdown conversion
- PDF script auto-detects text-based vs scanned pages and uses OCR only when needed
- All scripts support batch processing of entire folders
