from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.contrib.auth.models import User 
from django.conf import settings



class Course(models.Model):
    course_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="cors-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    course_code = models.CharField(max_length=25,unique=True)
    title = models.CharField(max_length=100, unique=True , null= False, blank= False)

    class Meta:
        verbose_name_plural = "Courses"
    
    def __str__(self):
        return self.title

class Year(models.Model):
    year_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="year-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    year = models.CharField(max_length=25,unique=True)

    class Meta:
        verbose_name_plural = "Years"

    def __str__(self):
        return self.year

class Subject(models.Model):
    sub_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="sub-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    sub_code = models.CharField(max_length=25,unique=True)
    title = models.CharField(max_length=100, null= False, blank= False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True,blank=True)

    class Meta:
        verbose_name_plural = "Subjects"
    
    def __str__(self):
        return self.title
    

class Institute(models.Model):
    institute_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="inst-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    institute_name = models.CharField(max_length=100, null= False, blank= False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)    

    class Meta:
        verbose_name_plural = "Institutes"
    

    def __str__(self):
        return self.institute_name
    
class Faculty(models.Model):
    fact_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="fact-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    faculty = models.CharField(max_length=100, null= False, blank= False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)    
    institute = models.ForeignKey(Institute, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Faculties"
    

    def __str__(self):
        return self.faculty
    
class Rbt(models.Model):
    rbt_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="rbt-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    rbt_level = models.CharField(max_length=100, unique=True , null= False, blank= False)
    rbt_value = models.IntegerField()

    class Meta:
        verbose_name_plural = "RBT Levels"
    

    def __str__(self):
        return self.rbt_level
    
class Marks(models.Model):
    mark_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="mark-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    marks = models.IntegerField()

    class Meta:
        verbose_name_plural = "Marks"
    
    def __str__(self):
        return str(self.marks)
    


class Questions(models.Model):
    question_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="ques-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    questions = models.CharField(max_length=500)
    rbt_level = models.ForeignKey(Rbt, on_delete=models.SET_NULL, null=True)
    added_by = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    marks = models.ForeignKey(Marks, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True,blank=True)
    

    class Meta:
        verbose_name_plural = "Questions"
    

    def __str__(self):
        return self.questions