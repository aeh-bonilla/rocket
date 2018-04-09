from django.db import models
from models import Tasks
import random
import requests
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpResponseServerError


JSON_FORMAT = 'application/json'
XML_FORMAT = 'text/xml'

@csrf_exempt
def say_hi(request):

    formato=request.META['HTTP_ACCEPT']

    if formato ==JSON_FORMAT:
        data = serializers.serialize("json",Tasks.objects.all())
    elif formato ==XML_FORMAT:
        data = serializers.serialize("xml", Tasks.objects.all())
    else:
        formato=JSON_FORMAT
        data = serializers.serialize("json", Tasks.objects.all())

    return HttpResponse(data, content_type=formato)

@csrf_exempt
def init_tasks(request):

    formato = request.META['HTTP_ACCEPT']

    init_tasks = []
    is_description = False
    description = None
    url_words = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(url_words)
    words = response.content.splitlines()

    for x in range(50):

        duration = random.randint(1,240)
        registered = random.randint(80, 101)

        while (is_description == False):

            position = random.randrange(len(words))
            description = words[position]
            is_description = get_description(description)

        try:
            task = Tasks(description=description,duration=duration, registered=registered,status='completada')
            task.save()
        except Exception:
            return HttpResponseServerError.status_code

        is_description = False

    if formato ==JSON_FORMAT:
        data = serializers.serialize("json",Tasks.objects.all())
    elif formato ==XML_FORMAT:
        data = serializers.serialize("xml", Tasks.objects.all())
    else:
        formato=JSON_FORMAT
        data = serializers.serialize("json", Tasks.objects.all())

    return HttpResponse(data, content_type=formato)

@csrf_exempt
def add_task(request):

    response = {}
    status = None
    description = request.POST.get('description')
    duration = request.POST.get('duration')

    try:
        task = Tasks(description=description,duration=int(duration), status='pendiente')
        task.save()
    except Exception:
         return HttpResponseServerError.status_code

    response ={'id':task.id,'status':'added'}

    return JsonResponse(response)

@csrf_exempt
def update_task(request):

    response = {}
    is_updated = False
    task_id = request.POST.get('id_task')
    description = request.POST.get('description')
    duration = request.POST.get('duration')
    registered = request.POST.get('registered')
    status = request.POST.get('status')

    try:
        task = Tasks.objects.get(pk=int(task_id))

        if task.status == 'pendiente':
            task.description = description
            task.duration = int(duration)
            task.registered = int(registered)
            task.status = status
            task.save()
            is_updated = True

    except Exception:
         return HttpResponseServerError.status_code

    response = {'id':task.id,'status': status,'updated':is_updated}

    return JsonResponse(response)

@csrf_exempt
def delete_task(request):

    task_id = request.POST.get('id')

    try:
        task = Tasks.objects.get(pk=int(task_id))
        task.delete()
    except Exception:
        return HttpResponseServerError.status_code

    response ={'id':task_id,'status':'deleted'}

    return JsonResponse(response)

@csrf_exempt
def list_tasks_by_description(request,q=None):

    tasks = []
    formato = request.META['HTTP_ACCEPT']

    try:
        task_list = Tasks.objects.filter(description__icontains=q)

        if formato ==JSON_FORMAT:
            data = serializers.serialize("json",task_list)
        elif formato ==XML_FORMAT:
            data = serializers.serialize("xml",task_list)
        else:
            formato=JSON_FORMAT
            data = serializers.serialize("json",task_list)

    except Exception,e:
        return HttpResponseServerError(str(e))

    return HttpResponse(data, content_type=formato)

@csrf_exempt
def list_task_by_status(request, status=None):

    tasks = []
    formato = request.META['HTTP_ACCEPT']

    try:
        task_list = Tasks.objects.filter(status=status)

        if formato ==JSON_FORMAT:
            data = serializers.serialize("json",task_list)
        elif formato ==XML_FORMAT:
            data = serializers.serialize("xml",task_list)
        else:
            formato=JSON_FORMAT
            data = serializers.serialize("json",task_list)

    except Exception,e:
        return HttpResponseServerError(str(e))

    return HttpResponse(data, content_type=formato)

def get_description(description):

    task = None
    is_description = False

    try:
        task = Tasks.objects.get(description=description)
    except Tasks.DoesNotExist:
        description = None

    if task == None:
        is_description = True

    return is_description
