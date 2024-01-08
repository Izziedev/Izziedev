# Generated by Django 3.2.7 on 2024-01-08 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_updatemodels'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='address',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='apartment_name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='apartment',
            name='location',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='apartment',
            name='number_of_rooms',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='room',
            name='room_description',
            field=models.TextField(default='', max_length=600),
        ),
        migrations.AddField(
            model_name='room',
            name='room_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='room_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='description',
            field=models.TextField(default='', max_length=600),
        ),
    ]