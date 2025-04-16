from django.db import models
from profiles.models import User
from core.base_model import BaseModel

class Location(BaseModel):
    """
    Model for storing location information.
    """
    location = models.CharField(max_length=100, unique=True,db_index=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
        
    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name_plural = 'Locations'
