# Generated by Django 2.0 on 2019-01-01 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20181222_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material_detail',
            name='material_name',
        ),
        migrations.AddField(
            model_name='material',
            name='material_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Material_detail'),
        ),
        migrations.AddField(
            model_name='material_detail',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]