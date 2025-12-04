from django.contrib import admin
from .models import HeroSection, Service, PortfolioItem, TeamMember, Contact, Career

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at']
    list_editable = ['status']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_at']
    list_editable = ['status']

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_at']
    list_editable = ['status']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'status', 'created_at']
    list_editable = ['status']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status', 'created_at', 'is_resolved']
    list_editable = ['status', 'is_resolved']

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'is_active', 'created_at']
    list_editable = ['status', 'is_active']