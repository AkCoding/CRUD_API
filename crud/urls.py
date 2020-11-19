from django.contrib import admin
from django.urls import path
from local_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.LCStudentAPI.as_view()),
    path('studentapi/<int:pk>', views.RUDStudentAPI.as_view()),
]
