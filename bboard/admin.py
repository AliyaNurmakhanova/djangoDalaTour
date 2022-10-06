from django.contrib import admin
from .models import *

# @admin.register(Bb)
#
# @admin.register(Location)

class CityAdmin(admin.ModelAdmin):
    list_display = ('id','city_name')
    list_filter = ('id','city_name')
admin.site.register(City,CityAdmin)

# class LocationInline(admin.TabularInline):
#     extra = 0
#     model = Location
#
# class CityAdmin(admin.ModelAdmin):
#     inlines = [LocationInline]
#     list_display = ('city_name')
# admin.site.register(City,CityAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'city_id')
admin.site.register(Location,LocationAdmin)

class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'route_category', 'place_on_the_route')
admin.site.register(Route,RouteAdmin)

class Ticket_for_routeAdmin(admin.ModelAdmin):
    list_display = ('route_id', 'ticket_price')
admin.site.register(Ticket_for_route,Ticket_for_routeAdmin)

class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'location_id', 'hotel_category', 'hotel_room', 'room_price', 'route_id')
admin.site.register(Hotel,HotelAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'balance')
admin.site.register(Client,ClientAdmin)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'location_id', 'route_id', 'total_price')
admin.site.register(Ticket,TicketAdmin)