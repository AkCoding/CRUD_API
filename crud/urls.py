from django.contrib import admin
from django.urls import path, include
from local_api import views
from rest_framework.routers import DefaultRouter
from local_api.auth import CustomAuthToken


router = DefaultRouter()

router.register('studentapi', views.StudentModelViewset, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', CustomAuthToken.as_view())
]
