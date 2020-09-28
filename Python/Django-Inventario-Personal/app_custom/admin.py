from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group, Permission

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        ('Nome do Usuário', {'fields': ('username',)}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'groups', 'is_superuser'),
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'get_group', 'is_staff',)
    list_display_links = ('username', 'email', 'first_name', 'last_name', 'get_group',)
    filter_horizontal = ['groups']

    def get_group(self, obj):
        return ' | '.join([p.name for p in obj.groups.all()])
    get_group.short_description = 'Grupos'


@admin.register(Group)
class GroupAdmin(GroupAdmin):
    list_display = ('name', 'get_perm')
    filter_vertical = ['permissions']

    def get_perm(self, obj):
        return ' | '.join([p.name for p in obj.permissions.all()])
    get_perm.short_description = 'Permissões'


@admin.register(Permission)
class PermAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'name',)
