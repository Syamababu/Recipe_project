from django.contrib import admin
from django.urls import path,include
from apiapp.views import comapnyviewset,comapnyviewsetdetails,company_list,company_details,CustomAuthTokenlogin
from apiapp.views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'employee',EmployeeViewSet)

urlpatterns = [
    path('api/', comapnyviewset.as_view()),
    path('api/<int:pk>/', comapnyviewsetdetails.as_view()),
    path('emp/',include(router.urls)),
    path('deco/',company_list),
    path('deco/<int:pk>/',company_details),
    path('auth/',CustomAuthTokenlogin.as_view())


]
EmployeeViewSet