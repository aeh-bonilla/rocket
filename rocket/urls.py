from django.conf.urls import url
from .views import say_hi, init_api, add_task, update_task, delete_task, list_tasks_by_description, list_task_by_status

app_name = 'rocket'

urlpatterns = [
    url(r'^api/hi/', say_hi, name='say_hi'),
    url(r'^api/init_api/', init_api, name='init_api'),
    url(r'^api/search/(?P<q>[\w-]+)/$', list_tasks_by_description, name='list_tasks_by_description'),
    url(r'^api/search_status/(?P<q>[\w-]+)/$', list_task_by_status, name='list_tasks_by_status'),
    url(r'^api/add_task/', add_task, name='add_task'),
    url(r'^api/update_task/', update_task, name='update_task'),
    url(r'^delete_task/', delete_task, name='delete_task')
]