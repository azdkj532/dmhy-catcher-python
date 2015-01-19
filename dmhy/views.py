import json

from django.http import HttpResponse
from dmhy.models import Task, Source, CheckQueuingSource

def tasklist( request ):
    if request.method == 'GET':
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
    elif request.method == 'POST':
        if request.user.is_authenticated():
            data = {}
            alias = keywords = ''
            try:
                data = json.loads( request.body.decode('utf-8') )
                alias = data.get('alias')
                keywords = data.get('keywords')
                Task( alias=alias, keywords=keywords ).save()
            except:
                return HttpResponse( json.dumps({"status":False}), content_type="application/json" )
            else:
                return HttpResponse( json.dumps({"status":True}) , content_type="application/json" )

def exec(request):
    if request.user.is_authenticated():
        CheckQueuingSource()
        task_list = models.Task.objects.filter( status=True )
        for task in task_list:
            task.executeTask()

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

from dmhy.dmhy import Search
def search( request ):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', '')
        topic_list = Search( keyword )
        return HttpResponse( json.dumps( topic_list ), content_type="application/json" )
    else:
        return HttpResponse( json.dumps({"message":"Please use GET method"}), content_type="application/json"  )

