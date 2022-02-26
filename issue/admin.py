from django.contrib import admin
from .models import Issue


# Register your models here.


class IssueAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content')


admin.site.register(Issue, IssueAdmin)
