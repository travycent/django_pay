from django.db import models
from core.base_model import BaseModel
from profiles.models import User
from system.models import Location


class Category(BaseModel):
   """
   Model for internet bundle categories.
   """ 
   name=models.CharField(
       max_length=100,
       help_text="e.g Daily, Weekly, Monthly, etc"
       )
   owner=models.ForeignKey(User,on_delete=models.CASCADE,db_index=True)
   
   
   def __str__(self):
       return self.name
   
   def get_owner(self):
        return self.owner.site_name
   get_owner.short_description = 'Owner'
   
   class Meta:
       verbose_name_plural = 'Internet Bundles'
       

class Packages(BaseModel):
    """
    Model for internet packages.
    """
    category=models.ForeignKey(Category,on_delete=models.CASCADE,db_index=True)
    amount=models.IntegerField()
    time=models.CharField(max_length=100)
    speed=models.CharField(default='-',max_length=25)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,db_index=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.amount
    
    def get_owner(self):
        return self.category.owner.site_name
    get_owner.short_description = 'Owner'
    
    class Meta:
        verbose_name_plural = 'Packages'
        
        
class SMS(BaseModel):
    """
    Model for SMS packages.
    """
    phone_number=models.CharField(max_length=15)
    message=models.TextField()
    
    def __str__(self):
        return self.phone_number
    
    class Meta:
        verbose_name_plural = 'SMS'
        
        
class Vouchers(BaseModel):
    """
    Model for storing voucher codes.
    """
    code=models.CharField(max_length=100,unique=True,db_index=True)
    used=models.BooleanField(default=False)
    package=models.ForeignKey(Packages,on_delete=models.CASCADE,db_index=True)
    
    def __str__(self):
        return self.code
    
    def get_owner(self):
        return self.package.category.owner.site_name
    get_owner.short_description = 'Owner'
    
    def get_package(self):
        return self.package.category.name
    get_package.short_description = 'Package'
    
    def get_location(self):
        return self.package.location.location
    get_location.short_description = 'Location'
    
    class Meta:
        verbose_name_plural = 'Vouchers'
    
   

