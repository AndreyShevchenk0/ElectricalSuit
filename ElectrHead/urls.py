from django. urls import path
from . import views
#from .views import index


urlpatterns = [
    #path('', index),
    path('', views.index, name='base'),
    path('myJob/', views.xer, name='myJob'),
]