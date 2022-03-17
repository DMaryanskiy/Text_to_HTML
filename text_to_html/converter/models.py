from django.db import models
from ckeditor.fields import RichTextField


class Converter(models.Model):
    """ model for ckeditor text widget """
    body = RichTextField(null=True, blank=True)
