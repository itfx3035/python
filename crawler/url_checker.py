#!/usr/bin/python

import urllib2

def url_check(url):
    url_to_check = url
    if url[:4].upper()!='HTTP':
        url_to_check = 'http://'+url_to_check
    try:
        urllib2.urlopen(url_to_check)
        return True
    except:
        return False