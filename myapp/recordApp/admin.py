from django.contrib import admin

from .models import Application, Status

# Register Application Model.
admin.site.register(Application)

# Register Status Model.
admin.site.register(Status)
