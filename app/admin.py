from django.contrib import admin

from app.models import ODS, D_Date, D_Type, D_Geographie, F_Dose

# Register your models here.
admin.site.register(ODS)
admin.site.register(D_Date)
admin.site.register(D_Type)
admin.site.register(D_Geographie)
admin.site.register(F_Dose)
