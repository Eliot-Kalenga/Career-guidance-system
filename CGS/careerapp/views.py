from django.shortcuts import render
from django.views.generic import View
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.utils import timezone

# Create your views here.
cluster1 = CareerCluster.objects.get(id = 1)

cluster2 = CareerCluster.objects.get(id = 2)

cluster3 = CareerCluster.objects.get(id = 3)

cluster4 = CareerCluster.objects.get(id = 4)

cluster5 = CareerCluster.objects.get(id = 5)

cluster6 = CareerCluster.objects.get(id = 7)

cluster7 = CareerCluster.objects.get(id = 8)

cluster8 = CareerCluster.objects.get(id = 9)

cluster9 = CareerCluster.objects.get(id = 10)

cluster10 = CareerCluster.objects.get(id = 11)

cluster11 = CareerCluster.objects.get(id = 12)

cluster12 = CareerCluster.objects.get(id = 13)

cluster13 = CareerCluster.objects.get(id = 14)

cluster14 = CareerCluster.objects.get(id = 15)

cluster15 = CareerCluster.objects.get(id = 16)

cluster16 = CareerCluster.objects.get(id = 17)


#school1 = school.objects.get(id = 1)
#school3 = school.objects.get(id = 3)
#school4 = school.objects.get(id = 4)
#school5 = school.objects.get(id = 5)
#school6 = school.objects.get(id = 6)
#school7 = school.objects.get(id = 7)


#def register(request):
 #   if request.method == 'POST':
  #      form = UserCreationForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return HttpResponseRedirect('/accounts/register/complete')

    #else:
     #   form = UserCreationForm()
    #token = {}
    #token.update(csrf(request))
    #token['form'] = form

    #return render_to_response('registration/registration_form.html', token)

#def registration_complete(request):
 #   return render_to_response('registration/registration_complete.html')
#login_required(login_url="login/")
def about(request):
     return render(request, 'careerapp/about.html', {})

def help(request):
     return render(request, 'careerapp/help.html', {})

# This function-based view handles the requests to the root URL /. See
# urls.py for the mapping.
def registration_form(request):
  # If the request method is POST, it means that the form has been submitted
  # and we need to validate it.
  if request.method == 'POST':
    # Create a RegistrationForm instance with the submitted data
    form = RegistrationForm(request.POST)
    
    # is_valid validates a form and returns True if it is valid and
    # False if it is invalid.
    if form.is_valid():
      # The form is valid and you could save it to a database
      # by creating a model object and populating the
      # data from the form object, but here we are just
      # rendering a success template page.
      return render(request, 'careerapp/success.html')
 
 # This means that the request is a GET request. So we need to
 # create an instance of the RegistrationForm class and render it in
 # the template
  else:
   form = RegistrationForm()
 
 # Render the registration form template with a RegistrationForm instance. If the
 # form was submitted and the data found to be invalid, the template will
 # be rendered with the entered data and error messages. Otherwise an empty
 # form will be rendered. Check the comments in the registration_form.html template
 # to understand how this is done.
  return render(request, 'careerapp/registration_form.html',
                { 'form' : form })


#@login_required(login_url="login/")
def	index(request):
	return	render(request, 'careerapp/index.html', {})

#@login_required(login_url="login/")
def self_assessment(request):
	return render(request, 'careerapp/self_assessment.html', {})

class EnterGrades(View):
    form_class = GradesForm
    template_name = 'careerapp/enter_grades.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        data = []
        form = self.form_class(request.POST)
        allprog = Programme.objects.all()
        programmes = {}
        facultys = []
        institutions = []

        context = {'form': form, 'data': data, 'allprog':allprog, 'programmes':programmes, 'facultys':facultys, 'institutions':institutions,}

        if form.is_valid():

            for i in range(6):
                data.append(form.cleaned_data['grade%s' %i])

            for i in allprog:

                if set(i.prereq.all()) < set(data):
                    programmes.update({str(i.name):str(i.faculty.school.name)})
                    facultys.append(str(i.faculty.school.name))

            return render(request, 'careerapp/programmes.html', context)
        return render(request, self.template_name, context)




class Entercourses(View):
    f_class = coursesForm
    t_name = 'careerapp/enter_course.html'

    def get(self, request, *args, **kwargs):
        form = self.f_class()
        return render(request, self.t_name, {'form': form})

    def post(self, request, *args, **kwargs):
        data = []
        form = self.f_class(request.POST)
        allprog = course.objects.all()
        programmes = {}
        facultys = []
        institutions = []

        context = {'form': form, 'data': data, 'allprog':allprog, 'programmes':programmes, 'facultys':facultys, 'institutions':institutions,}

        if form.is_valid():

            for i in range(6):
                data.append(form.cleaned_data['course%s' %i])

            for i in allprog:

                if set(i.career.all()) < set(data):
                    courses.update({str(i.name):str(i.faculty.school.name)})
                    facultys.append(str(i.faculty.school.name))

            return render(request, 'careerapp/Careerpath.html', context)
        return render(request, self.t_name, context)




class DisplayInstitutions(View):
    fo_class = InstitutionsForm
    te_name = 'careerapp/school.html'

    def get(self, request, *args, **kwargs):
        form = self.fo_class()
        return render(request, self.te_name, {'form': form})

   
    #@login_required(login_url="login/")
    
class ChooseInterests(View):
    form_class = ClusterForm
    template_name = 'careerapp/career_interests.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        activities = ClusterActivity.objects.all()
        paths = CareerPathway.objects.all()
        data = {}
        zipped = []
        mylist = {}
        clusters = []
        sorted_clusters = []
        form = self.form_class(request.POST)
        context = {'form': form, 'data': data, 'clusters':clusters, 'sorted_clusters':sorted_clusters,
                    'activities': activities, 'mylist': mylist}

        if form.is_valid():
            for i in range(1, 16):
                data.update({'cluster%s' %i: form.cleaned_data['cluster%s' %i]})

            #sort the dictionary
            for k in sorted(data, key = lambda k:len(data[k]), reverse=True):
                if (len(data[k])!=0):
                    sorted_clusters.append(k)
            for i in sorted_clusters:
                clusters.append(str(eval(i+'.name')))
            for i in clusters:
                mylist.update({clusters.index(i): i})

            return render(request, 'careerapp/careers.html', context)
        return render(request, self.template_name, context)

#@login_required(login_url="login/")
def viewcareers(request):
	empty = {}
	for i in range(1, 5):
		empty.update({'cluster%s' %i:  CareerPathway.objects.get(pk=i)})

	return render(request, 'careerapp/care.html', {'cluster1':cluster1, 'empty':empty})

#@login_required(login_url="login/")
def institutions(request):
	return render(request, 'careerapp/institutions.html')

#def post(self, request, *args, **kwargs):
 #       facultys = facultys.objects.all()
  #      programmes = programmes.objects.all()
   #     data = {}
    #    zipped = []
     #   mylist = {}
      #  schools = []
       # sorted_schools = []
        #form = self.form_class(request.POST)
        #context = {'form': form, 'data': data, 'schools':school, 'sorted_schools':sorted_schools,
         #           'faculties': faculties, 'mylist': mylist}
        #if form.is_valid():
         #   for i in range(1, 7):
          #      data.update({'school%s' %i: form.cleaned_data['school%s' %i]})

def programmes(request):
  return render(request, 'careerapp/programmes.html')