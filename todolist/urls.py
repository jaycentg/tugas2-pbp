from django.urls import path
from todolist.views import delete_task, login_user, register, show_todolist, logout_user, create_task, delete_task, change_status

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('delete/<int:id>', delete_task, name='delete'),
    path('change/<int:id>', change_status, name='change')
]