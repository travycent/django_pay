from django.contrib import admin
from profiles.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin




class UsersAdmin(BaseUserAdmin):
    list_display= ('site_name','email','first_name','last_name','phone_number','is_active','is_staff','updated_at')
    search_fields = ('site_name','email','first_name','last_name','phone_number',)
    list_filter = ('is_staff', 'is_active','created_at','updated_at')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','phone_number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'site_name', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'first_name', 'last_name', 'phone_number', 'site_name',  'password1', 'password2','is_superuser','is_staff', 'is_active', 'groups', 'user_permissions'),
    }),
    )

    
    ordering = ('email',)
    filter_horizontal = ()
    list_per_page = 50
admin.site.register(User,UsersAdmin)
