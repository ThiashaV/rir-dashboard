# Generated by Django 3.2.8 on 2021-10-19 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_sitepreferences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Harvester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvester_class', models.CharField(help_text='The type of harvester that will be used.Use class with full package.', max_length=100)),
                ('is_run', models.BooleanField(default=False, help_text='Is the harvester running.')),
                ('active', models.BooleanField(default=True, help_text='Make this harvester ready to be harvested.')),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('show_in_traffic_light', models.BooleanField(default=True, help_text='Showing this indicator on traffic light.')),
                ('unit', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('aggregation_behaviour', models.CharField(choices=[('All geography required in current time window', 'All geography required in current time window'), ('Use all available populated geography in current time window', 'Use all available populated geography in current time window'), ('Most recent for each geography', 'Most recent for each geography')], default='Use all available populated geography in current time window', max_length=256)),
                ('aggregation_method', models.CharField(choices=[('Aggregate data by sum all data.', 'Aggregate data by sum all data.'), ('Aggregate data by majority data in the levels.', 'Aggregate data by majority data in the levels.')], default='Aggregate data by sum all data.', max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndicatorFrequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('frequency', models.IntegerField(help_text='Frequency in days. This is used by harvester as a frequency to get new indicator data.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndicatorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndicatorValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='The date of the value harvested.', verbose_name='Date')),
                ('value', models.FloatField()),
                ('geometry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.geometry')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rir_data.indicator')),
            ],
            options={
                'ordering': ('-date',),
                'unique_together': {('indicator', 'date', 'geometry')},
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScenarioLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('level', models.IntegerField(unique=True)),
                ('color', models.CharField(blank=True, help_text='Put the hex color with # (e.g. #ffffff) or put the text of color. (e.g. blue)', max_length=16, null=True)),
                ('background_color', models.CharField(blank=True, help_text='Put the hex color with # (e.g. #ffffff) or put the text of color. (e.g. blue)', max_length=16, null=True)),
            ],
            options={
                'ordering': ('level',),
            },
        ),
        migrations.AddField(
            model_name='indicator',
            name='frequency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rir_data.indicatorfrequency'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='geometry_reporting_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.geometrylevel'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rir_data.indicatorgroup'),
        ),
        migrations.CreateModel(
            name='HarvesterLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True, help_text='This is when the harvester is started.')),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Error', 'Error'), ('Done', 'Done')], default='Running', max_length=100)),
                ('note', models.TextField(blank=True, null=True)),
                ('harvester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rir_data.harvester')),
            ],
            options={
                'ordering': ('-start_time',),
            },
        ),
        migrations.AddField(
            model_name='harvester',
            name='indicator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rir_data.indicator'),
        ),
        migrations.CreateModel(
            name='ProgramIntervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intervention_url', models.TextField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rir_data.program')),
                ('scenario_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rir_data.scenariolevel')),
            ],
            options={
                'unique_together': {('program', 'scenario_level')},
            },
        ),
        migrations.CreateModel(
            name='IndicatorValueExtraData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of attribute', max_length=100)),
                ('value', models.TextField(default=True, help_text='The value of attribute', null=True)),
                ('indicator_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rir_data.indicatorvalue')),
            ],
            options={
                'unique_together': {('indicator_value', 'name')},
            },
        ),
        migrations.CreateModel(
            name='IndicatorScenarioRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('rule', models.CharField(help_text='Use formula to create the rule and use x as the value.Example: x<100. It will replace x with the value and will check the condition.', max_length=256)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rir_data.indicator')),
                ('scenario_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rir_data.scenariolevel')),
            ],
            options={
                'unique_together': {('indicator', 'scenario_level')},
            },
        ),
        migrations.CreateModel(
            name='HarvesterAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of attribute', max_length=100)),
                ('value', models.TextField(default=True, help_text='The value of attribute', null=True)),
                ('harvester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rir_data.harvester')),
            ],
            options={
                'unique_together': {('harvester', 'name')},
            },
        ),
    ]