from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('sort/', views.sort),
    path('<int:pk>', views.Detail.as_view()),
    path('<int:pk>/update', views.NewData.as_view()),
    path('<int:pk>/delete', views.Delete.as_view())
]
