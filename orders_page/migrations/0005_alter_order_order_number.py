# Generated by Django 4.0.3 on 2022-05-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_page', '0004_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='66463', max_length=50),
        ),
    ]