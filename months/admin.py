from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.


@admin.register(January)
class January(admin.ModelAdmin):
    list_display = [field.name for field in January._meta.fields]
    # search_fields = ('date')


@admin.register(February)
class February(admin.ModelAdmin):
    list_display = [field.name for field in February._meta.fields]
    # search_fields = ('date')


@admin.register(March)
class March(admin.ModelAdmin):
    list_display = [field.name for field in March._meta.fields]
    # search_fields = ('date')


@admin.register(April)
class April(admin.ModelAdmin):
    list_display = [field.name for field in April._meta.fields]
    # search_fields = ('date')


@admin.register(May)
class May(admin.ModelAdmin):
    list_display = [field.name for field in May._meta.fields]
    # search_fields = ('date')


@admin.register(June)
class June(admin.ModelAdmin):
    list_display = [field.name for field in June._meta.fields]
    # search_fields = ('date')


@admin.register(July)
class July(admin.ModelAdmin):
    list_display = [field.name for field in July._meta.fields]
    # search_fields = ('date')


@admin.register(August)
class August(admin.ModelAdmin):
    list_display = [field.name for field in August._meta.fields]
    # search_fields = ('date')


@admin.register(September)
class September(admin.ModelAdmin):
    list_display = [field.name for field in September._meta.fields]
    # search_fields = ('date')


@admin.register(October)
class October(admin.ModelAdmin):
    list_display = [field.name for field in October._meta.fields]
    # search_fields = ('date')


@admin.register(November)
class November(admin.ModelAdmin):
    list_display = [field.name for field in November._meta.fields]
    # search_fields = ('date')


@admin.register(December)
class December(admin.ModelAdmin):
    list_display = [field.name for field in December._meta.fields]
    # search_fields = ('date')
