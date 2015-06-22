from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)

    def __str__(self):      # = ToString() in C sharp
        return self.name


class Inventory(models.Model):
    class Meta:
        verbose_name_plural = 'Inventories'
    item_name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor)
    part_number = models.IntegerField()
    warning_threshold = models.IntegerField()
    on_floor_quantity = models.IntegerField(default=0)
    in_warehouse_quantity = models.IntegerField(default=0)

    def __str__(self):      # = ToString() in C sharp
        return self.item_name

    def total_quantity(self):
        return self.on_floor_quantity + self.in_warehouse_quantity


class ShipmentStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Shipment(models.Model):
    status = models.ForeignKey(ShipmentStatus)
    vendor = models.ForeignKey(Vendor)
    items = models.ManyToManyField(Inventory)