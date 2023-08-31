from django.db import models

class blogpost(models.Model):
  title = models.CharField(max_length=255)
  content = models.CharField(max_length=255)
  pub_date = models.DateField()

class product(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  price = models.IntegerField()
  author = models.CharField(max_length=255, null=True)

  