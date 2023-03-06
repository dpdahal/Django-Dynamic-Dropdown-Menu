from django.contrib import admin

# Register your models here.

from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'parent']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['parent']
    search_fields = ['name', 'url']
