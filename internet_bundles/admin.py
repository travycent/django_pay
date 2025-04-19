from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','get_owner','created_at','updated_at')
    search_fields = ('name',)
    list_filter = ('created_at','updated_at')
    ordering = ('created_at',)
    
    # Hide the Owner field in the admin form
    exclude = ('owner',)
    
    # Modify the save method to automatically pick the owner
    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        super().save_model(request, obj, form, change)
        
    # show only only categories of the logged in user if they are not superuser
    def get_queryset(self,request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)
    
class PackagesAdmin(admin.ModelAdmin):
    list_display = ('category','amount','time','speed','location','updated_at','created_at')
    search_fields = ('category','amount','time','speed','location',)
    list_filter = ('created_at','updated_at')
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Packages,PackagesAdmin)
admin.site.register(SMS)
admin.site.register(Vouchers)

