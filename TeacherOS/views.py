from django.shortcuts import render
from models import *
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DetailView
from forms import *
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class home(ListView):
    template_name = "home.html"
    model = HomeWork
    fields = '__all__'

    def get_context_data(self, **kwargs):
            context = super(home , self).get_context_data(**kwargs)
            context['Act'] = Activities.objects.all()
            context['Rep'] = Reports.objects.all()
            context['Cla'] = Class.objects.all()
            return context

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
	success_url = reverse_lazy('home')


	def form_valid(self, form):
		user = form.save()
		return super(RegisterClass, self).form_valid(form)

        def get_context_data(self, **kwargs):
            context = super(RegisterClass, self).get_context_data(**kwargs)
            context['Students'] = Student.objects.all()
            return context

class RegisterActivitie(FormView):
	template_name = 'activitieform.html'
	form_class = ActivitiesForm
	#fields = ['user_perfil', 'mail', 'phone']
	success_url = reverse_lazy('home')


	def form_valid(self, form):
		user = form.save()
		return super(RegisterActivitie, self).form_valid(form)

        def get_context_data(self, **kwargs):
            context = super(RegisterActivitie, self).get_context_data(**kwargs)
            context['Students'] = Student.objects.all()
            return context

class RegisterHW(FormView):
	template_name = 'hwform.html'
	form_class = HWForm
	#fields = ['user_perfil', 'mail', 'phone']
	success_url = reverse_lazy('home')


	def form_valid(self, form):
		user = form.save()
		return super(RegisterHW, self).form_valid(form)

        def get_context_data(self, **kwargs):
            context = super(RegisterHW, self).get_context_data(**kwargs)
            context['Classes'] = Class.objects.all()
            return context

class RegisterReport(FormView):
	template_name = 'reportform.html'
	form_class = ReportForm
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		user = form.save()
		return super(RegisterReport, self).form_valid(form)

        def get_context_data(self, **kwargs):
                context = super(RegisterReport, self).get_context_data(**kwargs)
                context['Parents'] = User.objects.all()
                context['Students'] = Student.objects.all()
                return context


class RegisterStudent(FormView):
        template_name = 'studentform.html'
        form_class = StudentForm
        success_url = reverse_lazy('home')

        def form_valid(self, form):
                p = Student()
                p.Name = form.cleaned_data['Name']
                p.LastName = form.cleaned_data['LastName']
                p.Parent = form.cleaned_data['Parent']
                p.save()
                return super(RegisterStudent, self).form_valid(form)

        def get_context_data(self, **kwargs):
            context = super(RegisterStudent , self).get_context_data(**kwargs)
            # Add in a QuerySet of all the books
            context['Parents'] = User.objects.all()
            return context
