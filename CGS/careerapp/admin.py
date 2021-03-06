from django.contrib import admin
from .models import *

# Register your models here.
class FacultyInline(admin.StackedInline):
    model = Faculty
    extra = 7

class SchoolAdmin(admin.ModelAdmin):
    inlines = [FacultyInline]

class ProgrammeInline(admin.StackedInline):
    model = Programme
    extra = 6

class courseInline(admin.StackedInline):
    model = course
    extra = 6

class prerequisite_courseAdmin(admin.ModelAdmin):
    inlines = [courseInline]
    

class corequisite_courseAdmin(admin.ModelAdmin):
    inlines = [courseInline]
    


class FacultyAdmin(admin.ModelAdmin):
    inlines = [ProgrammeInline]


class CareerPathwayInline(admin.StackedInline):
    model = CareerPathway
    extra = 6



class ClusterActivityInline(admin.StackedInline):
    model = ClusterActivity
    extra = 7


class CareerClusterAdmin(admin.ModelAdmin):
    inlines = [CareerPathwayInline, ClusterActivityInline]


class courseAdmin(admin.StackedInline):

    inlines = [courseInline]

#class ProgrammeAdmin(admin.StackedInline):
   # inlines = [CareerClusterInline]


admin.site.register(School, SchoolAdmin)

admin.site.register(Faculty, FacultyAdmin)

admin.site.register(Programme)

admin.site.register(course)

admin.site.register(Subject)

admin.site.register(Prerequisite_course)

admin.site.register(corequisite_course)

admin.site.register(Prerequisite)

admin.site.register(CareerCluster)

admin.site.register(CareerPathway)

#admin.site.register(course, CareerPathway)
 