from django.contrib import admin
from .models import PC


class PCAdmin(admin.ModelAdmin):
    list_display = ("name", "race", "pc_class", "age")  # Customize the displayed fields


# Register the PC model with its corresponding Admin class
admin.site.register(PC, PCAdmin)
