from django.contrib import admin

from .models import green_card, blue_card, table, user

admin.site.register(green_card)
admin.site.register(blue_card)
admin.site.register(table)
admin.site.register(user)