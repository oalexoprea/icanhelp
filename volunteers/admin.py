from django.contrib import admin
from .models import Volunteer
from .models import Location
from .models import Availability
from .models import Status
from .models import Role

admin.site.register(Volunteer)
admin.site.register(Location)
admin.site.register(Availability)
admin.site.register(Status)
admin.site.register(Role)