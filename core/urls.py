from django.urls import path

from core import views

urlpatterns = [
    path('tasks/create/', views.TaskViewSet.as_view({'post': 'create'})),
    path('tasks/<str:identifier>/', views.TaskViewSet.as_view({'get': 'retrieve'})),
]
