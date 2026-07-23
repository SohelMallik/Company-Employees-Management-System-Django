from django.contrib import admin
from django.urls import include, path

from api.views import CompanyViewsset, EmployeeViewset
from rest_framework.routers import DefaultRouter

#Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'companies', CompanyViewsset, basename='companies')
#Registrer the employee viewset with the router

router.register(r'employees', EmployeeViewset, basename='employees')
urlpatterns = [
    path('', include(router.urls)),

]