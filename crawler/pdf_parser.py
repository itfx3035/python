#!/usr/bin/python

import PyPDF2
import re

def collect_urls(file_stream):
    try:
        pfile = PyPDF2.PdfFileReader(file_stream)
        num_pages = pfile.numPages
    except:
        num_pages = 0        
    res = []
    for pn in range(num_pages):
        txt = pfile.getPage(pn).extractText()
        tmp_res = re.findall(r'(https?:\/\/\S+\.\S+|www\.\S+\.\S+)', str(txt))
        res = res + tmp_res
    return res