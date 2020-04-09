from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('dpt', 'dpt_code', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('dpt', 'password')}),
        ('dpt info', {'fields': ('dpt_code',)}),
        ('Permissions', {'fields': ('is_admin','is_active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('dpt', 'dpt_code', 'password1', 'password2')}
         ),
    )
    search_fields = ('dpt',)
    ordering = ('dpt',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)