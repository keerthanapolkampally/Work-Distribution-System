from django.db import models
from index.models import Profile
from django.urls import reverse
import datetime

class project(models.Model):
	project_name = models.CharField(max_length=100)
	start_date = models.DateField(default=datetime.date.today)
	end_date = models.DateField(default=datetime.date.today)
	#team_leader = models.ForeignKey(Profile, on_delete = models.PROTECT)
	employee = models.ManyToManyField(Profile, blank = True, null = True)

	def get_absolute_url(self):
		return reverse('project:det', kwargs={'pk' : self.pk})
	def __str__(self):
		return self.project_name