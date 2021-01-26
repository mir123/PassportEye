'''
PassportEye::Util: PDF processing utilities.

Author: Konstantin Tretyakov
License: MIT
'''

import sys
from pdf2image import convert_from_path, convert_from_bytes
import io

def extract_first_jpeg_in_pdf(fstream):
    """
    Convert the first page of the PDF to JPG for further processing.
    I'm testing this as opposed to the PDFMiner way in the original PassportEye as I found it unreliable
    This works ok so far, of course only on one page of the PDF
    If I understood byte streams properly this would be for sure nicer
    
    by mir 2020-01-26
    """
    imdata = convert_from_bytes(fstream.read(), fmt='jpeg', dpi=300, jpegopt={'quality': 100}, first_page=1, last_page=1 )
    img_byte_arr = io.BytesIO()
    imdata[0].save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr
