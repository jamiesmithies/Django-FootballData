from django.contrib import admin
from basic_app.models import UserProfileInfo
from import_export.admin import ImportExportModelAdmin
from .models import Team

# Register your models here.

@admin.register(Team,UserProfileInfo)
class LeagueAdmin(ImportExportModelAdmin):
    pass
