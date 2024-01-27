# # projectapp/models.py
# from django.db import models

# class YourModel(models.Model):
#     field1 = models.CharField(max_length=255)
#     field2 = models.IntegerField()
#     # Add other fields as needed

from django.db import models

class projectapp(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    about = models.CharField(max_length=200)

    def __str__(self):
        return self.name
