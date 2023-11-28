from django.contrib import admin
from my_app.models import *
# Register your models here.
admin.site.register(GYM)
admin.site.register(Trainer)
admin.site.register(Client)
admin.site.register(WorkoutSession)
