from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser, Agent

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('mobile','email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile', 'password1', 'password2'),
        }),
    )
    list_display = ('mobile','email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('mobile','email', 'first_name', 'last_name')
    ordering = ('mobile',)

@admin.register(Agent)
class AgentAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('mobile','email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile', 'password1', 'password2'),
        }),
    )
    list_display = ('mobile','email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('mobile','email', 'first_name', 'last_name')
    ordering = ('mobile',)

admin.site.unregister(Group)
