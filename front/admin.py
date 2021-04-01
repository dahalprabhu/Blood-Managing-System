from django.contrib import admin
from .models import bloodmanagement
from .models import cust
from .models import campaign
from .models import redcross_donater
from .models import hackersclub_donater


admin.site.register(bloodmanagement)
admin.site.register(cust)
admin.site.register(campaign)
admin.site.register(redcross_donater)
admin.site.register(hackersclub_donater)


