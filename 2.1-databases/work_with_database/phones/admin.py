from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'release_date')
    prepopulated_fields = {"slug": ("name",)}
# Register your models here.
