from rest_framework import serializers

from .models import BoatOwner, Boat, Load, Agent, Order, OrderLoad


class BoatSerializer(serializers.ModelSerializer):
    boat_owner = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Boat
        fields = [
            'id',
            'name',
            'quantity',
            'fish_type',
            'boat_owner',
        ]


class BoatOwnerSerializer(serializers.ModelSerializer):
    boats = BoatSerializer(many=True)

    class Meta:
        model = BoatOwner
        fields = [
            'id',
            'name',
            'boats',
            'tilapia_sum',
            'mackerel_sum',
            'grouper_sum',
            'get_absolute_url',
        ]


class LoadSerializer(serializers.ModelSerializer):

    boat = BoatSerializer()

    class Meta:
        model = Load
        fields = [
            'id',
            'boat',
            'delivery_date',
            'batch_no',
            'format_delivery_date',
            'expiration_date',
            'get_absolute_url',
        ]


class AgentSerializer(serializers.ModelSerializer):
    load = LoadSerializer()

    class Meta:
        model = Agent
        fields = [
            'id',
            'name',
            'load',
            'join_date',
            'agent_id',
        ]


class OrderSerializer(serializers.ModelSerializer):
    agent = AgentSerializer()

    class Meta:
        model = Order
        fields = [
            'id',
            'agent',
            'ordered_at',
            'order_id',
        ]


class OrderLoadSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = OrderLoad
        fields = [
            'id',
            'order',
            'quantity',
            'fish_type',
            'pending',
        ]
