from django.db import models

# Create your models here.

class Document(models.Model):
  title = models.CharField(max_length=200, blank=False, null=False)
  doc_id = models.CharField(max_length=200, blank=False, null=False)
  author = models.CharField(max_length=200, blank=False, null=False)
  publication_date = models.CharField(max_length=200, blank=False, null=False)
  category = models.CharField(max_length=200, blank=False, null=False)
  summary = models.CharField(max_length=25000, blank=True, null=False)
  keywords = models.CharField(max_length=200, blank=True, null=False)

  def __str__(self):
      return self.title