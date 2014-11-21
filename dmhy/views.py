from django.http import HttpResponse
from django.http import HsonResponse
from dmhy.models import *
import json

def tasklist( request ):
    json_data = {}
    json_data['tasklist'] = []
    try:
        for task in Task.objects.all():
            json_data['tasklist'].append({
                "tid": task.tid,
                "alias": task.alias,
                "status": task.status,
                "last_update": str(task.last_update) 
                })
    except:
        json_data['status'] = False
    else:
        json_data['status'] = True

    return HttpResponse( json.dumps(json_data), content_type="application/json" )

def resourcelist( request, tid=0 ):
    json_data = {}
    json_data['resource'] = [{}]
    try:
        for resource in Source.objects.filter( tid=tid ).order_by("title"):
            json_data['resource'].append({
                "title": resource.title,
                "date": str( resource.date )
                })
    except:
        json_data['status'] = False
    else:
        json_data['status'] = True

    return HttpResponse( json.dumps(json_data), content_type="application/json" )

def records( request ):
    source_list = Source.objects.order_by("date").reverse()
    record_list = []
    for source in source_list:
        record_list.append({ 'title':source.title ,'date':str(source.date) })
    return HttpResponse( json.dumps(record_list), content_type="application/json" ) 

from dmhy.dmhyBot import Search
def search( request ):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        topic_list = Search( keyword )
        return JsonResponse( topic_list )
    else:
        return JsonResponse( {"message":"Please use POST method"} )

