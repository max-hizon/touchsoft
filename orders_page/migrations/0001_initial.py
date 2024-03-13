# Generated by Django 4.0.3 on 2022-05-24 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(default='26628', max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('product_quantity', models.CharField(max_length=50)),
                ('branch_choice', models.CharField(choices=[('k', 'Katipunan branch'), ('m', 'Makati branch')], max_length=1)),
                ('user_name', models.CharField(max_length=100)),
                ('shipping_address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
            ],
        ),
    ]
