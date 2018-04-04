from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
	path('<str:project_url_name>/', views.project_view, name = 'project_view')
]