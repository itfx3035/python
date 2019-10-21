This is a PoC pdf crawler. The main goal is to collect all URL links from uploaded pdf file.

Assumptions:
1. FILE_UPLOAD_MAX_MEMORY_SIZE left by default (2.5Mb), so large files can be temporary stored
2. Assuming valid urls are started with "HTTP:\\", "HTTPS:\\" and "www."
3. Assuming all urls should be separated from other text with space or caret return.
4. url_alive boolean field added to db
5. No error handling provided for REST api. Possible errors: 
    - doc_id REST parameter wasn't supplied
    - document with specified id wasn't found


Prerequisites:
1. Python 2.7
2. PyPDF2 library

Usage:
POST​ ​/ FILE UPLOAD​: http://ip:port/uploads/
GET / JSON​ (set of all the of documents): http://ip:port/get_all_docs/
GET / JSON​ (set of URLs for a specific document): http://ip:port/get_doc_urls/?doc_id=N
GET / JSON​ (set of all URLs found): http://ip:port/get_all_urls/
