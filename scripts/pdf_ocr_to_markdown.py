#!/usr/bin/env python3
"""
PDF OCR to Markdown Converter

Converts scanned PDFs (image-based) to Markdown using OCR.
Also handles text-based PDFs by extracting text directly.

Usage:
    python pdf_ocr_to_markdown.py input.pdf [output.md]
    python pdf_ocr_to_markdown.py /path/to/folder  # Batch convert all .pdf files

Requirements:
    pip install pymupdf pytesseract Pillow

    For OCR functionality, Tesseract must be installed:
    - Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki
    - Mac: brew install tesseract
    - Linux: sudo apt-get install tesseract-ocr

Notes:
    - Text-based PDFs are extracted directly (fast, accurate)
    - Image-based/scanned PDFs use OCR (slower, may need quality tuning)
    - The script auto-detects which method to use per page
"""

import sys
import os
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF not installed. Run: pip install pymupdf")
    sys.exit(1)

# OCR imports (optional - only needed for scanned PDFs)
try:
    import pytesseract
    from PIL import Image
    import io
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False


def extract_text_from_page(page):
    """
    Extract text from a PDF page.
    Returns tuple: (text, method_used)
    """
    # Try direct text extraction first
    text = page.get_text("text").strip()

    # If we got substantial text, use it
    if len(text) > 50:  # Arbitrary threshold
        return text, "text"

    # Otherwise, try OCR if available
    if OCR_AVAILABLE:
        try:
            # Render page to image
            pix = page.get_pixmap(dpi=300)
            img_data = pix.tobytes("png")
            img = Image.open(io.BytesIO(img_data))

            # Run OCR
            ocr_text = pytesseract.image_to_string(img).strip()

            if ocr_text:
                return ocr_text, "ocr"
        except Exception as e:
            print(f"  OCR failed: {e}")

    # Return whatever text we got (might be empty)
    return text, "text" if text else "none"


def clean_text_for_markdown(text):
    """Clean extracted text for Markdown formatting."""
    lines = text.split('\n')
    cleaned_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            cleaned_lines.append("")
            continue

        # Basic cleanup
        # Remove excessive whitespace
        line = ' '.join(line.split())

        cleaned_lines.append(line)

    # Remove excessive blank lines (more than 2 in a row)
    result = []
    blank_count = 0
    for line in cleaned_lines:
        if line == "":
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
        else:
            blank_count = 0
            result.append(line)

    return '\n'.join(result)


def convert_pdf_to_markdown(input_path, output_path=None):
    """
    Convert a PDF file to Markdown.

    Args:
        input_path: Path to the .pdf file
        output_path: Optional output path. If None, uses input filename with .md extension

    Returns:
        Path to the output file
    """
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() != '.pdf':
        raise ValueError(f"Input file must be a .pdf file: {input_path}")

    # Determine output path
    if output_path is None:
        output_path = input_path.with_suffix('.md')
    else:
        output_path = Path(output_path)

    # Open PDF
    doc = fitz.open(str(input_path))

    # Build Markdown content
    md_parts = []

    # Document title (from filename or PDF metadata)
    doc_title = doc.metadata.get('title', '') or input_path.stem
    doc_title = doc_title.replace("_", " ").replace("-", " ").title()
    md_parts.append(f"# {doc_title}")
    md_parts.append(f"*Converted from: {input_path.name}*")

    # Add metadata if available
    author = doc.metadata.get('author', '')
    if author:
        md_parts.append(f"*Author: {author}*")

    md_parts.append("---")

    # Track extraction methods used
    methods_used = {"text": 0, "ocr": 0, "none": 0}

    # Process each page
    total_pages = len(doc)
    for page_num, page in enumerate(doc, start=1):
        print(f"  Processing page {page_num}/{total_pages}...", end=" ")

        text, method = extract_text_from_page(page)
        methods_used[method] += 1
        print(f"({method})")

        if text:
            # Add page header for multi-page documents
            if total_pages > 1:
                md_parts.append(f"## Page {page_num}")

            cleaned_text = clean_text_for_markdown(text)
            md_parts.append(cleaned_text)

            if total_pages > 1:
                md_parts.append("---")

    doc.close()

    # Write output
    markdown_content = "\n\n".join(md_parts)
    output_path.write_text(markdown_content, encoding='utf-8')

    # Summary
    print(f"Converted: {input_path.name} -> {output_path.name}")
    print(f"  Pages: {total_pages} (text: {methods_used['text']}, ocr: {methods_used['ocr']}, empty: {methods_used['none']})")

    return output_path


def batch_convert(folder_path):
    """Convert all .pdf files in a folder."""
    folder = Path(folder_path)

    if not folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder}")

    pdf_files = list(folder.glob("*.pdf"))

    if not pdf_files:
        print(f"No .pdf files found in {folder}")
        return []

    converted = []
    for pdf_file in pdf_files:
        try:
            print(f"\nProcessing: {pdf_file.name}")
            output_path = convert_pdf_to_markdown(pdf_file)
            converted.append(output_path)
        except Exception as e:
            print(f"Error converting {pdf_file.name}: {e}")

    print(f"\nConverted {len(converted)} of {len(pdf_files)} files")
    return converted


def check_dependencies():
    """Check and report on available dependencies."""
    print("Dependency Check:")
    print(f"  PyMuPDF (fitz): OK")

    if OCR_AVAILABLE:
        print(f"  pytesseract: OK")
        print(f"  Pillow: OK")

        # Check if Tesseract binary is available
        try:
            version = pytesseract.get_tesseract_version()
            print(f"  Tesseract binary: OK (version {version})")
        except Exception:
            print(f"  Tesseract binary: NOT FOUND")
            print("    Install Tesseract for OCR support:")
            print("    - Windows: https://github.com/UB-Mannheim/tesseract/wiki")
            print("    - Mac: brew install tesseract")
            print("    - Linux: sudo apt-get install tesseract-ocr")
    else:
        print(f"  pytesseract: NOT INSTALLED (OCR disabled)")
        print(f"  Pillow: NOT INSTALLED (OCR disabled)")
        print("    Run: pip install pytesseract Pillow")

    print()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print()
        check_dependencies()
        sys.exit(1)

    if sys.argv[1] == "--check":
        check_dependencies()
        sys.exit(0)

    input_path = Path(sys.argv[1])

    # Check if input is a directory (batch mode) or single file
    if input_path.is_dir():
        batch_convert(input_path)
    else:
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        convert_pdf_to_markdown(input_path, output_path)


if __name__ == "__main__":
    main()
