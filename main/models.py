from django.db import models
from dateutil.relativedelta import *
from django.db.models import Sum
from autoslug import AutoSlugField


FISH_TYPE = [
    ('tilapia', 'Tilapia'),
    ('mackerel', 'Mackerel'),
    ('grouper', 'Grouper')
]


class BoatOwner(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')

    def tilapia_sum(self):
        sum = BoatOwner.objects.filter(pk=self.pk, boats__fish_type='tilapia').aggregate(Sum('boats__quantity'))
        return sum['boats__quantity__sum']

    def mackerel_sum(self):
        sum = BoatOwner.objects.filter(pk=self.pk, boats__fish_type='mackerel').aggregate(Sum('boats__quantity'))
        return sum['boats__quantity__sum']

    def grouper_sum(self):
        sum = BoatOwner.objects.filter(pk=self.pk, boats__fish_type='grouper').aggregate(Sum('boats__quantity'))
        return sum['boats__quantity__sum']

    def get_absolute_url(self):
        return f'/{self.pk}/{self.slug}/'


class Boat(models.Model):
    boat_owner = models.ForeignKey(BoatOwner, related_name='boats', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    fish_type = models.CharField(max_length=50, choices=FISH_TYPE)

    def __str__(self):
        return self.name


class Load(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/{self.pk}/'

    def format_delivery_date(self):
        return self.delivery_date.strftime('%b,%d %Y @ %H:%M')

    def batch_delivery_date(self):
        return self.delivery_date.strftime('%m-%d-%Y-at-%H-%M')

    def batch_no(self):
        return f'{self.boat.name}-{self.batch_delivery_date()}-{self.boat.fish_type}'

    def expiration_date(self):
        date = self.delivery_date + relativedelta(months=+8)
        return date.strftime('%b,%d %Y @ %H:%M')


class Agent(models.Model):
    name = models.CharField(max_length=50)
    load = models.ForeignKey(Load, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def join_date(self):
        return self.date.strftime('%b,%d %Y @ %H:%M')

    def agent_id(self):
        return self.date.strftime('%m%d%y%H%M%S')


class Order(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def ordered_at(self):
        return self.date.strftime('%b,%d %Y @ %H:%M')

    def order_id(self):
        return self.date.strftime('%m%d-%Y%H-%M%S')


class OrderLoad(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    fish_type = models.CharField(max_length=50, choices=FISH_TYPE)
    pending = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        tilapia_sum = Boat.objects.filter(fish_type='tilapia').aggregate(Sum('quantity'))
        mackerel_sum = Boat.objects.filter(fish_type='mackerel').aggregate(Sum('quantity'))
        grouper_sum = Boat.objects.filter(fish_type='grouper').aggregate(Sum('quantity'))

        if self.quantity > tilapia_sum['quantity__sum'] and self.fish_type == 'tilapia':
            self.pending = True

        if self.quantity > mackerel_sum['quantity__sum'] and self.fish_type == 'mackerel':
            self.pending = True

        if self.quantity > grouper_sum['quantity__sum'] and self.fish_type == 'grouper':
            self.pending = True

        super(OrderLoad, self).save(*args, **kwargs)
