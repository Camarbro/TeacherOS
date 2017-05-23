from django.conf.urls import url, include
from .views import home, login

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'login', login, name = 'login'),
]
