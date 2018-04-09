from django.conf.urls import url
from .views import say_hi, init_tasks, add_task, update_task, delete_task, list_tasks_by_description, list_task_by_status

app_name = 'rocket'

urlpatterns = [
    url(r'^api/hi/', say_hi, name='say_hi'),
    url(r'^api/init_tasks/', init_tasks, name='init_tasks'),
    url(r'^api/search/(?P<q>[\w-]+)/$', list_tasks_by_description, name='list_tasks_by_description'),
    url(r'^api/search_status/(?P<status>[\w-]+)/$', list_task_by_status, name='list_tasks_by_status'),
    url(r'^api/add_task/', add_task, name='add_task'),
    url(r'^api/update_task/', update_task, name='update_task'),
    url(r'^api/delete_task/', delete_task, name='delete_task')
]