from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Projects(models.Model):
    title = models.CharField(max_length=200, default='Title here')
    description = models.TextField(default='Description here')
    image = models.ImageField(upload_to='project_pic/')
    create_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    github_url = models.URLField(
        blank=True, default='https://www.addlinkhere.com')

    def get_absolute_url(self):
        return reverse('projects_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Certificates(models.Model):
    images = models.ImageField(upload_to='certificates_images/')
    title = models.CharField(max_length=200, default='Title here')

    def get_absolute_url(self):
        return reverse('certificates_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
