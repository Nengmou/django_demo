# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=100)),
                ('part_number', models.IntegerField()),
                ('warning_threshold', models.IntegerField()),
                ('on_floor_quantity', models.IntegerField(default=0)),
                ('in_warehouse_quantity', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('items', models.ManyToManyField(to='inventory.Inventory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShipmentStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shipment',
            name='status',
            field=models.ForeignKey(to='inventory.ShipmentStatus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='vendor',
            field=models.ForeignKey(to='inventory.Vendor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inventory',
            name='vendor',
            field=models.ForeignKey(to='inventory.Vendor'),
            preserve_default=True,
        ),
    ]
