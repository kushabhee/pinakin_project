from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HeroSectionViewSet, ServiceViewSet, PortfolioItemViewSet,
    TeamMemberViewSet, ContactViewSet, CareerViewSet
)

router = DefaultRouter()
router.register(r'heroes', HeroSectionViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'portfolio', PortfolioItemViewSet)
router.register(r'team', TeamMemberViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'careers', CareerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
