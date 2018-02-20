from django.contrib import admin
from  .models import Servei, Actiu, Seguiment, Ips
# Register your models here.

admin.site.register(Servei)
admin.site.register(Actiu)
admin.site.register(Seguiment)
admin.site.register(Ips)

admin.site.site_title = "Pla de Contingencia"
admin.site.site_header = "Pla de Contingecia AjSVC"
