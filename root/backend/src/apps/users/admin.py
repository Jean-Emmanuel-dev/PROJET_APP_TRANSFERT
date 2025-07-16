from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'phone_number', 'is_verified', 'is_staff', 'date_joined')
    ordering = ('-date_joined',)
    search_fields = ('email', 'phone_number')
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'password')}),
        ('Permissions', {'fields': ('is_verified', 'is_staff', 'is_superuser')}),
        ('Dates', {'fields': ('date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password1', 'password2', 'is_verified', 'is_staff', 'is_superuser'),
        }),
    )
