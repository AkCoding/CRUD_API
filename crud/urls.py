from django.contrib import admin
from django.urls import path
from local_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuinfo/', views.Student_detail),
    # path('stuinfo/<int:pk>', views.Student_detail),
    # path('stuinfo/', views.Student_list),
    # path('stucreate/', views.student_create),
]
