from django.urls import path , include
from .views import *
urlpatterns = [
    path("", List_View.as_view() , name="list-data")

]