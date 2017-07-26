from django.db import models

from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Biodata(models.Model):
	first_name = ArrayField(
        models.CharField(max_length=255, blank=True, null=True),
        size=1)

	def __str__(self):
		return self.first_name


