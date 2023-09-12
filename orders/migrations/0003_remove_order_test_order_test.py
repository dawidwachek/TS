# Generated by Django 4.2.1 on 2023-08-04 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='test',
        ),
        migrations.AddField(
            model_name='order',
            name='test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.item'),
            preserve_default=False,
        ),
    ]
