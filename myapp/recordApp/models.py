from django.db import models
from django.utils import timezone

# Application record
class Application(models.Model):
    organizationName = models.CharField(max_length=120)
    status = models.CharField(max_length=50)
    comments = models.CharField(max_length=300)
    link = models.CharField(max_length=500)
    dateApplied = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Org: {self.organizationName}, Status: {self.status} On {self.dateApplied}"
