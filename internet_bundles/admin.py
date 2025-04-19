from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Packages)
admin.site.register(SMS)
admin.site.register(Vouchers)

