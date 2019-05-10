from django.contrib import admin
from .models import MCUser,Survey,MCQuestion
# Register your models here.
admin.site.register(MCUser)
admin.site.register(Survey)
admin.site.register(MCQuestion)
