from django.contrib import admin
from .models import Question, Facility


# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('message', 'isFilter')


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('academicBuilding', 'facilityName', 'floor')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Facility, FacilityAdmin)
