from django.urls import path,include
from .views import *
urlpatterns = [
    path('feedback',create_feedback,name="create_feedback"),
    path('get',download_as_cvs,name="download_as_cvs")

]
