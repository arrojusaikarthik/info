from django.contrib import admin
from .models import alertsandnote, allorderslist, logos, ongoingridesnow
# Register your models here.
admin.site.register(ongoingridesnow)
admin.site.register(alertsandnote)
admin.site.register(logos)
admin.site.register(allorderslist)
