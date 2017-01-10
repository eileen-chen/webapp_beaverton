from django.conf.urls import url
#from .views import register
from . import views

urlpatterns = [
    #url(r'^register/', views.register, name='register'),
    url(r'^register$', views.register, name='register')
]