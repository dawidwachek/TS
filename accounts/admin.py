from django.contrib import admin

from .models import User, UserProxy

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_admin']
    fieldsets = [
        ('User general data', {
            'fields':('email', 'password')
        }),
        ('Permissions', {
            'fields':('is_admin','is_active','is_superadmin')
        })
        ]
    

@admin.register(UserProxy)
class UserProxyAdmin(admin.ModelAdmin):
    list_display = ['email','first_name', 'active_sub','first_step']
    fieldsets = [
        ('User data', {
            'fields':('email','first_name', 'date_birthday', 'phone_number','first_step')
            }
        ),
        ('Sub data', {
            'fields':('active_sub', 'id_sub')
            }
        ),
        
        ]