from django.conf.urls import url
from . import views

urlpatterns = [
	
    url(r'^$', views.index, name='index'),
    url(r'^careers/', views.viewcareers, name='viewcareers'),
    url(r'^institutions/', views.institutions, name='institutions'),
    url(r'^grades/', views.EnterGrades.as_view(), name='enter_grades'),
    url(r'^enter_course/', views.Entercourses.as_view(), name='enter_course'),
    url(r'^school/', views.DisplayInstitutions.as_view(), name='school'),
    #url(r'^programmes/*$', views.dislay_programmes, name='programmes'),
    url(r'^interests/', views.ChooseInterests.as_view(), name='career_interests'),
    url(r'^self_assessment/', views.self_assessment, name='self_assessment'),
    url(r'^registration_form/',views.registration_form, name='registration_form'),
    url(r'^about/',views.about, name='about'),
    url(r'^help/',views.help, name='help'),
    url(r'^programmes/',views.programmes, name='programmes')
   ] 
