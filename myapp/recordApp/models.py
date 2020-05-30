from django.db import models
from django.utils import timezone

# All possible status
class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Status: {self.status}"


# Application record
class Application(models.Model):
    organizationName = models.CharField(max_length=120)
    status = models.ForeignKey(Status, on_delete=models.SET("Status Deleted"), related_name="statusName")
    comments = models.CharField(max_length=300)
    link = models.CharField(max_length=500)
    dateApplied = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Org: {self.organizationName}, {self.status} On {self.dateApplied}"
