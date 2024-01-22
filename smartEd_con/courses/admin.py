from django.contrib import admin
from . models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','date','availabe')
    list_filter = ('date','availabe',)
    search_fields = ('name','date','availabe')