from django.contrib import admin
from core.models import *



class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id','course_code','title']

class YearAdmin(admin.ModelAdmin):
    list_display = ['year_id','year']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['sub_id','sub_code','course','title','year']

class InstituteAdmin(admin.ModelAdmin):
    list_display = ['institute_id','institute_name']

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['fact_id','faculty','institute']

class RBTAdmin(admin.ModelAdmin):
    list_display = ['rbt_id','rbt_level','rbt_value']

class MarksAdmin(admin.ModelAdmin):
    list_display = ['mark_id','marks']


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question_id','questions','course','subject','marks']




admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Rbt, RBTAdmin)
admin.site.register(Marks, MarksAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Year, YearAdmin)