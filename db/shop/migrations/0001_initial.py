# Generated by Django 2.2.3 on 2020-02-21 12:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Name')),
                ('type', models.TextField(blank=True, null=True, verbose_name='Type')),
                ('product', models.TextField(blank=True, null=True, verbose_name='Main product(s)')),
                ('kindergarten_supplier', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=3, null=True, verbose_name='Do kindergartens buy from here?')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('phone', models.TextField(blank=True, null=True, verbose_name='Telephone')),
                ('email', models.TextField(blank=True, null=True, verbose_name='E-mail')),
                ('website', models.TextField(blank=True, null=True, verbose_name='Website')),
                ('toggle', models.CharField(blank=True, choices=[('gps', 'Use GPS'), ('interactive', 'Point on Map'), ('manual', 'Enter Manually')], max_length=11, null=True, verbose_name='Location Mode')),
                ('geometry', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Location')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('accuracy', models.FloatField(blank=True, null=True, verbose_name='GPS Accuracy')),
            ],
            options={
                'verbose_name': 'shop',
                'verbose_name_plural': 'shops',
            },
        ),
    ]
