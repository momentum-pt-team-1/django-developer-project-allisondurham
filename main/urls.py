

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.todo_users, name='todo_users'),
    path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('todo/new/', views.todo_new, name='todo_new'),
    path('todo/<int:pk>/edit/', views.todo_edit, name='todo_edit'),
    path('todo/done/', views.todo_done, name='todo_done'),
    path('todo/user/', views.todo_user, name='todo_user'),
    path('todo/date/', views.todo_date, name='todo_date'),
    path('todo/users/', views.todo_users, name='todo_users'),
    path('todo/list/', views.todo_list, name='todo_list'),
    path('home', views.home, name='home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
