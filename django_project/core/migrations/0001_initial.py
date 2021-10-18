# Generated by Django 3.2.8 on 2021-10-18 03:50

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeometryLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('lower_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.geometrylevel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Geometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=512, unique=True)),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('alias', models.TextField(blank=True, help_text='Alias of the geometry name. Use comma separator for multi alias.', null=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('child_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geometry_child_of', to='core.geometry')),
                ('geometry_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.geometrylevel')),
            ],
        ),
    ]
