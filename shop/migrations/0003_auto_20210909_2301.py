# Generated by Django 3.1.7 on 2021-09-09 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_updateorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updateorder',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order'),
        ),
    ]
