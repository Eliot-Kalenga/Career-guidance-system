"""career URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from careerapp.forms import LoginForm
from careerapp.forms import RegistrationForm


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('careerapp.urls')),
    url(r'^login/$', views.login, {'template_name': 'careerapp/login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
     # Map the root URL / to be handled by 
      # 'registration.views.registration_form' view
      # url(r'^registeration_form/$', views.registration_form, {'template_name': 'careerapp/registration_form.html', 'authentication_form': RegistrationForm}),
      
      # Allow the URLs beginning with /captcha/ to be handled by
      # the urls.py of captcha module from 'django-simple-captcha'
    # url(r'^captcha/', include('captcha.urls')),

]
