from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Project

# Create your views here.

def project_view(request, project_url_name):
	
	project = get_object_or_404(Project, project_title = project_url_name)

	return render(request, 'projects/' + project_url_name.lower() + ".html", {'project':project})

	#return HttpResponse("This is the home page " + str(project_id))