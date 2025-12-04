from rest_framework import viewsets
from .models import HeroSection, Service, PortfolioItem, TeamMember, Contact, Career
from .serializers import (
    HeroSectionSerializer, ServiceSerializer, PortfolioItemSerializer,
    TeamMemberSerializer, ContactSerializer, CareerSerializer
)

class HeroSectionViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class PortfolioItemViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioItemSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.filter(is_active=True)  # Only show active careers
    serializer_class = CareerSerializer