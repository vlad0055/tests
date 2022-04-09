from django.db import models

class Test_data(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
    	return self.name
