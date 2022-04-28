from django.contrib import admin


from crmapp.models import ExtraService, CleaningSort, Service, PropertySort, \
    Client, Inventory, Cleanser, Fine, Bonus, \
    FineCategory, Order, ForemanReport, ForemanOrderUpdate, ExtraServiceOrder, ServiceOrder, Foreman, Cleaners, \
    InventoryInOrder, CleanserInOrder


class ExtraServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    fields = ['name', 'unit', 'price', 'cleaning_time']



admin.site.register(ExtraService, ExtraServiceAdmin)
admin.site.register(CleaningSort)
admin.site.register(Service)
admin.site.register(PropertySort)
admin.site.register(Client)
admin.site.register(Fine)
admin.site.register(FineCategory)
admin.site.register(Bonus)
admin.site.register(Inventory)
admin.site.register(Cleanser)
admin.site.register(Order)
admin.site.register(ForemanReport)
admin.site.register(ForemanOrderUpdate)
admin.site.register(ServiceOrder)
admin.site.register(ExtraServiceOrder)
admin.site.register(Foreman)
admin.site.register(Cleaners)
admin.site.register(InventoryInOrder)
admin.site.register(CleanserInOrder)

