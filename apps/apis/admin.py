from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import User


class InlineUser(admin.TabularInline):
    model = User
class UserAdmin(ImportExportModelAdmin):
    pass
admin.site.register(User, UserAdmin)
