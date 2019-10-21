# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pdf_parser import collect_urls
from models import mdocument, murl
from url_checker import url_check

def handle_uploaded_file(f):
    url_list = collect_urls(f)
    
    new_mdoc = mdocument(doc_name=f.name)
    new_mdoc.save()

    for url_link in url_list:
        curr_alive = url_check(url_link)
        new_url = murl(doc_id=new_mdoc, url=url_link, url_alive=curr_alive)
        new_url.save()
    
    
        
        