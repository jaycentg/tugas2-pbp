from django.urls import path
from todolist.views import delete_ajax, login_user, register, show_json, show_todolist, logout_user, create_task, delete_task, change_status, show_todolist_ajax
from todolist.views import add_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist_ajax, name='show_todolist_ajax'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('delete/<int:id>', delete_ajax, name='delete'),
    path('change/<int:id>', change_status, name='change'),
    path('json/', show_json, name='show-json'),
    path('add/', add_task_ajax, name='add-task-ajax'),
]