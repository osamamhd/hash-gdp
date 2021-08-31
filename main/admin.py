from django.contrib import admin
from .models import BoatOwner, Boat, Load, Agent, Order, OrderLoad

@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'fish_type', 'boat_owner']
@admin.register(BoatOwner)
class BoatOwnerAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Load)
class LoadAdmin(admin.ModelAdmin):
    list_display = ['boat', 'delivery_date', 'batch_no', ]


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'join_date',
        'agent_id',
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'agent',
        'ordered_at',
    ]


@admin.register(OrderLoad)
class OrderLoadAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'quantity',
        'fish_type',
        'pending',
    ]