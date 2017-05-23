from django.conf.urls import url, include
from .views import *
from django.contrib.auth.views import login, logout_then_login


urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'login', login, {'template_name': 'login.html'}, name = 'login'),
    url(r'^logout$', logout_then_login, name = "logout"),
    url(r'^hw_list$', HWView.as_view(), name ="hw" ),
    url(r'^activities$', ActivitiesView.as_view(), name ="activities" ),
    url(r'^reports$', ReportsView.as_view(), name = "reports"),
    url(r'^classes$', ClassVIew.as_view(), name="classes"),
    url(r'^signup$', Register.as_view(), name="signup"),
    url(r'^register_report$', RegisterReport.as_view(), name="register_report"),
    url(r'^register_student$', RegisterStudent.as_view(), name="register_student"),
    url(r'^register_class$', RegisterClass.as_view(), name="register_class"),
    url(r'^register_activitie$', RegisterActivitie.as_view(), name="register_activitie"),
    url(r'^register_homework$', RegisterHW.as_view(), name="register_homework")
]
