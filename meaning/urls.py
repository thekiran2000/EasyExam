from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="mainhome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUS"),
    path("notes/",views.notes,name="Notes"),
    path("transfield/",views.transfield,name="Transfield"),
    path("pro/",views.pro,name="pronounce"),
    path("result/",views.result,name="Result"),
    
  
]
