from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('reviewer/', views.reviewer, name="reviewer"),
    path('assessment/', views.assessment, name="assessment"),
    path('assessment/eye-dentify', views.first_assessment, name="assessment1"),
    path('assessment/eye-thought', views.second_assessment, name="assessment2"),
    path('assessment/eye-complete', views.third_assessment, name="assessment3"),
    path('assessment/eye-care', views.fourth_assessment, name="assessment4"),
]
