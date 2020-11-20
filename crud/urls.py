from django.contrib import admin
from django.urls import path, include
from local_api import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('studentapi', views.StudentReadOnlyModelViewset, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
