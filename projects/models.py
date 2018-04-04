from django.db import models

# Create your models here.

def image_location(image_name):
	return "projects/images/" + image_name

class Project(models.Model):
	project_title = models.CharField(max_length = 200)
	project_year = models.IntegerField()
	project_text = models.CharField(max_length = 2000)
	project_image_name = models.CharField(max_length = 100)

	def return_image(self):
		return image_location(self.project_image_name + ".jpeg")