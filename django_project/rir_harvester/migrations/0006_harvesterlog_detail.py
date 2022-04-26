# Generated by Django 3.2.8 on 2022-03-10 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rir_harvester', '0005_alter_harvester_harvester_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvesterlog',
            name='detail',
            field=models.TextField(blank=True, help_text='The detail of the harvesters. Should be filled with array so can construct the data in array.', null=True),
        ),
    ]