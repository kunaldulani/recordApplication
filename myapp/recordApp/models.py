from django.db import models
from django.utils import timezone
from .addToCalendar import addToCalendar

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
    reminderDate = models.DateField(default="2000-01-01", null=True, blank=True)
    reminderNote = models.CharField(max_length=3000, null=True, blank=True)
    attendeeEmail = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Org: {self.organizationName}, {self.status} On {self.dateApplied}"

    def save(self, *args, **kwargs):
        addToCalendar(self)
        super(Application, self).save(*args, **kwargs)
