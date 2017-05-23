from django.shortcuts import render
from models import *
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DetailView
from forms import *
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html')

class HWView(ListView):
    template_name = "hw.html"
    model = HomeWork
    fields = '__all__'

class ActivitiesView(ListView):
    template_name = "activities.html"
    model = Activities
    fields = '__all__'

class ReportsView(ListView):
    template_name = "reports.html"
    model = Reports
    fields = '__all__'

class ClassVIew(ListView):
    template_name = "classes.html"
    model = Class
    fields = '__all__'

class Register(FormView):
	template_name = 'register.html'
	form_class = User_form
	#fields = ['user_perfil', 'mail', 'phone']
	success_url = reverse_lazy('home')


	def form_valid(self, form):
		user = form.save()
		return super(Register, self).form_valid(form)

class RegisterClass(FormView):
	template_name = 'classform.html'
	form_class = ClassForm
	#fields = ['user_perfil', 'mail', 'phone']
	success_url = reverse_lazy('home')


	def form_valid(self, form):
		user = form.save()
		return super(RegisterClass, self).form_valid(form)

class RegisterActivitie(FormView):
	template_name = 'activitieform.html'
	form_class = ActivitiesForm
	#fields = ['user_perfil', 'mail', 'phone']
	success_url = reverse_lazy('home')


	def form_valid(self, form):
		user = form.save()
		return super(RegisterActivitie, self).form_valid(form)

class RegisterHW(FormView):
	template_name = 'hwform.html'
	form_class = HWForm
	#fields = ['user_perfil', 'mail', 'phone']
	success_url = reverse_lazy('home')


	def form_valid(self, form):
		user = form.save()
		return super(RegisterHW, self).form_valid(form)

class RegisterReport(FormView):
	template_name = 'reportform.html'
	form_class = ReportForm
	#fields = ['user_perfil', 'mail', 'phone']
	success_url = reverse_lazy('home')


	def form_valid(self, form):
		user = form.save()
		return super(RegisterReport, self).form_valid(form)

class RegisterStudent(FormView):
	template_name = 'studentform.html'
	form_class = StudentForm
	#fields = ['user_perfil', 'mail', 'phone']
	success_url = reverse_lazy('home')


	def form_valid(self, form):
		user = form.save()
		return super(RegisterStudent, self).form_valid(form)
