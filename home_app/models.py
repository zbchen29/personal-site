from django.db import models

from projects.models import Project

# Create your models here.

# Image URL retrieve; image_name should not include extensions like ".png"
def image_location(image_name):
	return "home_app/images/" + image_name

# Work experiences model
class Work(models.Model):
	work_title = models.CharField(max_length = 200)
	work_date = models.CharField(max_length = 200)
	work_text = models.CharField(max_length = 2000)
	work_image_name = models.CharField(max_length = 100)

	# Name convention: work_NAME

	def return_image(self):
		return image_location(self.work_image_name + ".jpeg")

	def __str__(self):
		return self.work_title

# Education/schools model
class Education(models.Model):
	education_title = models.CharField(max_length = 200)
	education_date = models.CharField(max_length = 200)
	education_text = models.CharField(max_length = 2000)
	education_image_name = models.CharField(max_length = 100)

	# Name convention: education_NAME

	def return_image(self):
		return image_location(self.education_image_name + ".jpeg")

	def __str__(self):
		return self.education_title

# Album model for artwork
class Album(models.Model):
	album_title = models.CharField(max_length = 200)
	album_year = models.IntegerField()
	album_text = models.CharField(max_length = 1000)
	album_image_name = models.CharField(max_length = 100)

	# Name convention: album_NAME
	
	def return_image(self):
		return image_location(self.album_image_name + ".jpeg")

	# Preview images have "_pv" suffix
	def return_png_preview(self):
		preview_name = self.album_image_name + "_pv.jpeg"
		return image_location(preview_name)

	def __str__(self):
		return self.album_title

# Individual artwork model
class Art(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	art_title = models.CharField(max_length = 200)
	art_text = models.CharField(max_length = 1000)
	art_image_name = models.CharField(max_length = 100)

	# Name convention: art_NAME_NUMBER
	# Wireframe renders: art_NAME_wf

	def return_image(self):
		return image_location(self.art_image_name + ".png")

	def __str__(self):
		return self.art_title

def remove_extensions(target_model):
	if target_model == Work:
		for temp_ob in target_model.objects.all():
			temp_ob.work_image_name = temp_ob.work_image_name[:len(temp_ob.work_image_name)-4]
			temp_ob.save()
	elif target_model == Education:
		for temp_ob in target_model.objects.all():
			temp_ob.education_image_name = temp_ob.education_image_name[:len(temp_ob.education_image_name)-4]
			temp_ob.save()
	elif target_model == Album:
		for temp_ob in target_model.objects.all():
			temp_ob.album_image_name = temp_ob.album_image_name[:len(temp_ob.album_image_name)-4]
			temp_ob.save()
	elif target_model == Art:
		for temp_ob in target_model.objects.all():
			temp_ob.art_image_name = temp_ob.art_image_name[:len(temp_ob.art_image_name)-4]
			temp_ob.save()