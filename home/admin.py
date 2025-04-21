from django.contrib import admin
from home.models import Person, Address, Club


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ("sin", "first_name", "last_name", "birthday", "address", "created", "updated")
    search_fields = ("sin", "first_name", "last_name")
    list_filter = ("created", "updated")


# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "province", "postal_code", "country")
    search_fields = ("street", "city", "province", "postal_code", "country")


class ClubAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Address, AddressAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Club, ClubAdmin)
