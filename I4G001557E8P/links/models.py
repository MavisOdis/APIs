from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

# Create your models here.
class Link(models.Model):
    target_url : models.URLField(max_length=200)
    description : models.CharField(max_length=200)
    identifier : models.SlugField(blank=True, unique=True)
    author : models.ForeignKey(get_user_model(),  on_delete=models.CASCADE, related_name='author')
    created_date : models.DateField(auto_created=True)
    active : models.BooleanField(True)

    def save(self, *args, **kwargs):
        self.identifier = slugify(self.description)
        super().save(*args, **kwargs)