from django.contrib import admin
from .models import CrudModel, ContactModel, AboutModel

# Register your models here.
admin.site.register(CrudModel)
admin.site.register(ContactModel)
admin.site.register(AboutModel)