from datetime import date, timezone

from django.db import models

# Create your models here.
from django.conf import settings


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, blank=True, null=False,
                                 related_name='departments_added')
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, blank=True, null=False,
                                    related_name='departments_modified')
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='departments_deleted')
    added_by_date = models.DateField(default=date.today)
    modified_by_date = models.DateField(default=date.today)
    deleted_by_date = models.DateField(blank=True, null=True)

    def delete(self):
        self.deleted_by_date = date.today()
        self.active=False
        self.save()
