from django.db import models
from django.utils import timezone


#class user(modes.mode):
  #  name = models.CharField(max_length=100)
   # username = models.CharField(max_length=100)
   # email = models.Emailfield(max_length=100)
   # password = models.CharField(max_length=50) 
  #  password = models.CharField(max_length=50)

     #def __str__(self):
      #  return self.name

class School(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Faculty(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey('School')

    def __str__(self):
        return self.name


#fix this
class Prerequisite(models.Model):
    subject = models.ForeignKey('Subject')
    points = models.IntegerField(default=6)


    def __str__(self):
        return self.subject.name

class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CareerPathway(models.Model):
    name = models.CharField(max_length=200)
    cluster = models.ForeignKey('CareerCluster', null=True)

    def __str__(self):
        return self.name


class Programme(models.Model):
    name = models.CharField(max_length=500)
    faculty = models.ForeignKey('Faculty')
    duration = models.IntegerField(default=4)
    prereq = models.ForeignKey(Subject, null=True, blank=True)
    career = models.ManyToManyField(CareerPathway, blank=True)
#
#class Admin:
 #   list_display = ('name')
  #  list_filter = ('name')
   # ordering = ('name',)
    #search_fields = ('name',)

    #def __str__(self):
     #   return self.name
class Prerequisite_course(models.Model):
    course_code = models.CharField(max_length=300, blank=True)
    course_name = models.CharField(max_length=300, blank=True)
       
    def __init__(self):
        return self.course_name
           
class corequisite_course(models.Model):
    course_code = models.CharField(max_length=300, blank=True)
    course_name = models.CharField(max_length=300, blank=True)
       
    def __init__(self):
        return self.course_name


class course(models.Model):
    course_code = models.CharField(max_length=300, blank=True)
    course_name = models.CharField(max_length=300, blank=True)
    Department = models.CharField(max_length=300, blank=True)
    faculty = models.ManyToManyField('Faculty')
    institution = models.ManyToManyField('School')
    Prerequisite = models.ManyToManyField(Prerequisite_course, blank=True)
    corequisite = models.ManyToManyField(corequisite_course, blank=True)

    def __str__(self):
        return self.course_code


class CareerCluster(models.Model):
    name = models.CharField(max_length=200)
    programme = models.ManyToManyField('Programme')
    info = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name

class ClusterActivity(models.Model):
    activity = models.TextField()
    cluster = models.ForeignKey('CareerCluster')

    def __str__(self):
        return self.activity

class Color(models.Model):
    name = models.CharField(max_length=200)
    Personality = models.ForeignKey('Personality')

    def __str__(self):
        return self.name

class Personality(models.Model):
    name = models.CharField(max_length=700)
    cluster = models.ManyToManyField('CareerCluster')
    
    def __str__(self):
        return self.name
