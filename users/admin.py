from django.contrib import admin
from .models import User,reponse,cop,registeruser

# Register your models here.

class adminregister(admin.ModelAdmin):
    list_display=['grade','nom','prenom','email','matricule','image','promotion','commandant_promotion','date','password']

admin.site.register(User)
admin.site.register(reponse)
admin.site.register(cop)
admin.site.register(registeruser,adminregister)