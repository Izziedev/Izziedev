# Generated by Django 3.2.7 on 2024-01-08 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_making_Room_and_Apartment_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='address',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='apartment_name',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='location',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='number_of_rooms',
        ),
        migrations.RemoveField(
            model_name='room',
            name='name',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_description',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_number',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_price',
        ),
    ]
