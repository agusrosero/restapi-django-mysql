from django.urls import path, include
from .views import CompanyView
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'clubs', views.ClubViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('companies/', CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>', CompanyView.as_view(), name='companies_process'),
]
