# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse,JsonResponse 
from upload import handle_uploaded_file
from forms import document_form
from django.views.decorators.csrf import csrf_exempt
from models import mdocument, murl
from django.db.models import Count
from json import JSONEncoder


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = document_form(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")  
    else:
        form = document_form()
    return render_to_response('uploads.html', {'form': form})


def get_all_docs(request):
    if request.method == 'GET': 
        data = mdocument.objects.annotate(num_urls=Count('murl'))
        resp = list()
        # TODO - serialize!
        for d in data:
            resp.append({'doc_id': d.id,'doc_name': d.doc_name, 'url_count': d.num_urls})
        return JsonResponse(resp, safe=False)

def get_all_urls(request):
    if request.method == 'GET': 
        data = murl.objects.all()
        resp = list()
        # TODO - serialize and move to separate module
        for u in data:
            resp.append({'doc_id': u.doc_id.id, 'url': u.url, 'url_alive': u.url_alive})
        return JsonResponse(resp, safe=False)

def get_doc_urls(request):
    if request.method == 'GET': 
        # TODO check if doc_id wasn't passed
        param_doc_id = request.GET.get('doc_id')
        # TODO check if param_doc_id not found
        doc = mdocument.objects.get(id=int(param_doc_id))
        data = murl.objects.filter(doc_id=doc)
        resp = list()
        # TODO - serialize and move to separate module
        for u in data:
            resp.append({'url': u.url, 'url_alive': u.url_alive})
        return JsonResponse(resp, safe=False)

