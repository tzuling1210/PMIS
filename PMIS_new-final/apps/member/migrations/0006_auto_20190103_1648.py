# Generated by Django 2.0 on 2019-01-03 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_product_price'),
        ('member', '0005_auto_20181213_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('total_price', models.PositiveIntegerField(blank=True, null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Product')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='products',
            field=models.ManyToManyField(blank=True, to='member.Transaction_product'),
        ),
    ]