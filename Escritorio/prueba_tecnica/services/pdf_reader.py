"""Módulo responsable de leer y extraer texto de archivos PDF."""

from typing import BinaryIO
from pypdf import PdfReader


def extract_text_from_pdf(pdf_file: BinaryIO) -> str:
    """
    Extract text from all pages of a PDF file.

    Args:
        pdf_file: A file-like object opened in binary mode containing PDF data.

    Returns:
        A single string containing all text extracted from the PDF.
        Returns an empty string if the PDF is empty or corrupted.

    Raises:
        No exceptions are raised. Errors are handled gracefully.
    """
    try:
        pdf_reader = PdfReader(pdf_file)
        
        # Check if PDF has pages
        if not pdf_reader.pages:
            return ""
        
        extracted_text = []
        
        # Extract text from each page
        for page_num, page in enumerate(pdf_reader.pages):
            try:
                page_text = page.extract_text()
                if page_text:
                    extracted_text.append(page_text)
            except Exception:
                # Skip pages that fail to extract
                continue
        
        # Join all extracted text with line breaks
        return "\n".join(extracted_text)
    
    except Exception:
        # Handle corrupted or invalid PDFs gracefully
        return ""
