from django.contrib import admin
from .models import Events,Venue,MyclubUser
# Register your models here.
admin.site.register(Venue)
admin.site.register(MyclubUser)
admin.site.register(Events)