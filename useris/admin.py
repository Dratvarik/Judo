from django.contrib import admin
from .models import Children, Groups, Season_tickets, Treners, Userss
# Register your models here.


class ChildrenAdmin(admin.ModelAdmin):
    list_display=('surname', 'name', 'middlename',  'date_of_birth', 'payment', 'date_of_pay', 'season_ticket', 'comments')
    list_display_links=('surname', 'name', 'middlename')
    search_fields=('surname', 'name', 'middlename',  'date_of_birth', 'payment', 'date_of_pay', 'season_ticket', 'comments')
    list_editable=('payment', )
    # list_filter=('is_published', 'category')

class GroupsAdmin(admin.ModelAdmin):
    list_display=('name_section', 'quantity_in_week', 'cost', 'FIO_coach')
    list_display_links=('name_section', )
    search_fields=('name_section', 'quantity_in_week', 'cost', 'FIO_coach')
    # list_editable=('payment', )
    # list_filter=('is_published', 'category')

class TrenersAdmin(admin.ModelAdmin):
    list_display=('surname', 'name', 'middlename', 'FIO_coach')
    list_display_links=('surname', 'name', 'middlename')

class Season_ticketsAdmin(admin.ModelAdmin):
    list_display=('season_ticket', )

class UserssAdmin(admin.ModelAdmin):
    list_display=('name', 'phone')


admin.site.register(Children, ChildrenAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Treners, TrenersAdmin)
admin.site.register(Season_tickets, Season_ticketsAdmin)
admin.site.register(Userss, UserssAdmin)