from django.contrib import admin

from chrono.models import Project, Task, Time

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Time)
