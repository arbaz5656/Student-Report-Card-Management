from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name="Home"),
    path('showmarks/<student_id>/',views.ShowMarks,name="ShowMarks")
]