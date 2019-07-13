from django.contrib import admin
from .models import Vendor,Packaging,Customer,Unit,Family,item

admin.site.register(Vendor)
admin.site.register(Packaging)
admin.site.register(Customer)
admin.site.register(Family)
admin.site.register(Unit)
admin.site.register(item)



# for registering the models in admin panel
