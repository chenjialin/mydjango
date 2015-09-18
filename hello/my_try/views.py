from django.shortcuts import render
from django.http import HttpResponse
from interface import *
import json
# Create your views here.


def index(request):
    return render(request, 'test.htm', {"key": "value"})


def grab_data(request):
    try:
        xml_data = get_xml_data()
        data_list = parse_xml(xml_data)
        save_to_db(data_list)
        json_data = {'0': 'success!'}
    except Exception,e:
        print e
        json_data = {'1': 'fail!'}
    return HttpResponse(json.dumps(json_data))


def show(request):

    return render(request, 'show.html', {})


def get_detail(request):
    data = get_data_from_db()
    return HttpResponse(json.dumps(data), content_type="aplication/json")

