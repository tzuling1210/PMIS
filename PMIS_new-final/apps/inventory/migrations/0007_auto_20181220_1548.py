# Generated by Django 2.0 on 2018-12-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20181220_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='number_needed',
        ),
        migrations.AddField(
            model_name='component',
            name='number_needed',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
