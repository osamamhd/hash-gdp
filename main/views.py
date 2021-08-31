from django.views.generic import ListView
from .models import BoatOwner, Boat, Load, Agent, Order, OrderLoad
from django.db.models import Sum
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import BoatOwnerSerializer, BoatSerializer, LoadSerializer, AgentSerializer, OrderSerializer, OrderLoadSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q

from rest_framework import generics
from rest_framework import mixins


class BoatListView(APIView):

    def get(self, request, format=None):
        boats = Boat.objects.all()
        serializer = BoatSerializer(boats, many=True)
        return Response(serializer.data)


class BoatOwnerListView(APIView):

    def get(self, request, format=None):
        boats = BoatOwner.objects.all()
        serializer = BoatOwnerSerializer(boats, many=True)
        return Response(serializer.data)


class BoatOwnerDetailView(APIView):

    serializer_class = BoatOwnerSerializer

    def get(self, request, pk, boat_owner_slug, format=None):
        boat = BoatOwner.objects.get(pk=pk, slug=boat_owner_slug)
        serializer = BoatOwnerSerializer(boat)
        return Response(serializer.data)


class BoatDetailView(APIView):

    serializer_class = BoatSerializer

    def get(self, request, pk, format=None):
        boat = Boat.objects.get(pk=pk)
        serializer = BoatSerializer(boat)
        return Response(serializer.data)


class LoadListView(APIView):

    def get(self, request, format=None):

        load = Load.objects.all()
        serializer = LoadSerializer(load, many=True)
        return Response(serializer.data)


class AgentListView(APIView):

    def get(self, request, format=None):

        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many=True)
        return Response(serializer.data)


class OrderListView(APIView):

    def get(self, request, format=None):

        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class LoadDetailView(APIView):

    serializer_class = LoadSerializer

    def get(self, request, pk, format=None):
        load = Load.objects.get(pk=pk)
        serializer = LoadSerializer(load)
        return Response(serializer.data)


class OrderLoadListView(APIView):

    def get(self, request, format=None):

        orderloads = OrderLoad.objects.all()
        serializer = OrderLoadSerializer(orderloads, many=True)
        return Response(serializer.data)


class PendingOrderLoad(APIView):

    def get(self, request, format=None):
        orderloads = OrderLoad.objects.filter(pending=True)
        serializer = OrderLoadSerializer(orderloads, many=True)
        return Response(serializer.data)


class DoneOrderLoad(APIView):

    def get(self, request, format=None):
        orderloads = OrderLoad.objects.filter(pending=False)
        serializer = OrderLoadSerializer(orderloads, many=True)
        return Response(serializer.data)


class OrderLoadDetailView(APIView):

    serializer_class = OrderLoadSerializer

    def get(self, request, pk, format=None):
        orderload = OrderLoad.objects.get(pk=pk)
        serializer = OrderLoadSerializer(orderload)
        return Response(serializer.data)


@api_view()
def tilapia_quantity(request):
    boat_sum = Boat.objects.filter(fish_type='tilapia').aggregate(Sum('quantity'))
    order_sum = OrderLoad.objects.filter(fish_type='tilapia', pending=False).aggregate(Sum('quantity'))
    if order_sum['quantity__sum']:
        sum = boat_sum['quantity__sum'] - order_sum['quantity__sum']
    else:
        sum = boat_sum['quantity__sum']
    return Response(sum)


@api_view()
def mackerel_quantity(request):
    boat_sum = Boat.objects.filter(fish_type='mackerel').aggregate(Sum('quantity'))
    order_sum = OrderLoad.objects.filter(fish_type='mackerel', pending=False).aggregate(Sum('quantity'))
    if order_sum['quantity__sum']:
        sum = boat_sum['quantity__sum'] - order_sum['quantity__sum']
    else:
        sum = boat_sum['quantity__sum']
    return Response(sum)


@api_view()
def grouper_quantity(request):
    boat_sum = Boat.objects.filter(fish_type='grouper').aggregate(Sum('quantity'))
    order_sum = OrderLoad.objects.filter(fish_type='grouper', pending=False).aggregate(Sum('quantity'))
    if order_sum['quantity__sum']:
        sum = boat_sum['quantity__sum'] - order_sum['quantity__sum']
    else:
        sum = boat_sum['quantity__sum']
    return Response(sum)


@api_view()
def tilapia_requested(request):
    order_sum = OrderLoad.objects.filter(fish_type='tilapia', pending=True).aggregate(Sum('quantity'))
    return Response(order_sum['quantity__sum'])


@api_view()
def mackerel_requested(request):
    order_sum = OrderLoad.objects.filter(fish_type='mackerel', pending=True).aggregate(Sum('quantity'))
    return Response(order_sum['quantity__sum'])


@api_view()
def grouper_requested(request):
    order_sum = OrderLoad.objects.filter(fish_type='grouper', pending=True).aggregate(Sum('quantity'))
    return Response(order_sum['quantity__sum'])


@api_view()
def tilapia_delivered(request):
    order_sum = Boat.objects.filter(fish_type='tilapia').aggregate(Sum('quantity'))
    return Response(order_sum['quantity__sum'])


@api_view()
def mackerel_delivered(request):
    order_sum = Boat.objects.filter(fish_type='mackerel').aggregate(Sum('quantity'))
    return Response(order_sum['quantity__sum'])


@api_view()
def grouper_delivered(request):
    order_sum = Boat.objects.filter(fish_type='grouper').aggregate(Sum('quantity'))
    return Response(order_sum['quantity__sum'])