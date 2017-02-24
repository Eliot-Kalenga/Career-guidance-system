from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *
# Import the CaptchaField from 'django-simple-captcha'
#from captcha.fields import CaptchaField

class GradesForm(forms.Form):
    grade0 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')
    grade1 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')
    grade2 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')
    grade3 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')
    grade4 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')
    grade5 = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Subject')

class coursesForm(forms.Form):
    course0 = forms.ModelChoiceField(queryset=course.objects.all(), label='Course 1')
    course1 = forms.ModelChoiceField(queryset=course.objects.all(), label='course 2')
    course2 = forms.ModelChoiceField(queryset=course.objects.all(), label='Course 3')
    course3 = forms.ModelChoiceField(queryset=course.objects.all(), label='Course 4')
    course4 = forms.ModelChoiceField(queryset=course.objects.all(), label='Course 5')
    course5 = forms.ModelChoiceField(queryset=course.objects.all(), label='Course 6')
    course6 = forms.ModelChoiceField(queryset=course.objects.all(), label='Course 7')
    course7 = forms.ModelChoiceField(queryset=course.objects.all(), label='Course 8')
    course8 = forms.ModelChoiceField(queryset=course.objects.all(), label='Course 9')
    course9 = forms.ModelChoiceField(queryset=course.objects.all(), label='Course 10')


class InstitutionsForm(forms.Form):
    Institution = forms.ModelChoiceField(queryset=School.objects.all(), label='College')

class ClusterForm(forms.Form):
    cluster1 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 1),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,
    )
    cluster2 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 2),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,)
    cluster3 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 3),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster4 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 4),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster5 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 5),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster6 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 7),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster7 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 8),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster8 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 9),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster9 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 10),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster10 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 11),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster11 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 12),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster12 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 13),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster13 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 14),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster14 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 15),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster15 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 16),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )
    cluster16 = forms.ModelMultipleChoiceField(
        queryset = ClusterActivity.objects.filter(cluster_id = 17),
        widget = forms.CheckboxSelectMultiple,
        label = '',
        required = False,    )

# Create form class for the Login form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type':'password'}))

# Create form class for the Registration form
class RegistrationForm(forms.Form):
  name = forms.CharField()
  username = forms.CharField()
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput) # Set the widget to
                                                         # PasswordInput
  password2 = forms.CharField(widget=forms.PasswordInput,
                              label="Confirm password") # Set the widget to
                                                        # PasswordInput and
                                                        # set an appropriate
                                                        # label
  #captcha = CaptchaField()
  
  # clean_<fieldname> method in a form class is used to do custom validation
  # for the field.
  # We are doing a custom validation for the 'password2' field and raising
  # a validation error if the password and its confirmation do not match
  def clean_password2(self):
    password = self.cleaned_data['password'] # cleaned_data dictionary has the
                                             # the valid fields
    password2 = self.cleaned_data['password2']
    if password != password2:
      raise forms.ValidationError("Passwords do not match.")
    return password2