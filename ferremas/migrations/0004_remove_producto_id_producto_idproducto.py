# Generated by Django 5.0.6 on 2024-05-21 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferremas', '0003_producto_marca_producto_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.AddField(
            model_name='producto',
            name='idproducto',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
