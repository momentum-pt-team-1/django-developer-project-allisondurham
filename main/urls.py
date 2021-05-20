

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('todo/new/', views.todo_new, name='todo_new'),
    path('todo/<int:pk>/edit/', views.todo_edit, name='todo_edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)