from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Work, Education, Album, Art
from projects.models import Project

# Create your views here.

def home(request):

	# Home slide variables
	home_title_text = "Zhenbang Chen"
	home_body_text = "Welcome to my site.  Please enjoy your stay."

	# Work slide variables
	work_list = Work.objects.all()

	# Education slide variables
	education_list = Education.objects.all()

	# Artwork slide variables
	album_list = Album.objects.all()

	# Project slide variables
	project_list = Project.objects.all()

	# About slide variables
	about_text = "This is the about slide text."

	context = {
		'home_title_text':	home_title_text,
		'home_body_text':	home_body_text,
		'work_list':		work_list,
		'education_list':	education_list,
		'album_list':		album_list,
		'project_list':		project_list,
		'about_text':		about_text
	}

	return render(request, 'home_app/index.html', context)
	
	#return HttpResponse("This is the home page")