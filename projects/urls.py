from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects,name='projects'),
    path('project/<str:pk>/',views.project,name='project'),
    path('create-Project/',views.createProject,name="create-project"),
    path('updateProject/<str:pk>/',views.updateProject,name="updateProject"),
    path('delete-project/<str:pk>/',views.deleteProject,name="deleteProject"),
]
