# Generated by Django 4.2.1 on 2023-08-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='test',
            field=models.ManyToManyField(blank=True, null=True, to='orders.item'),
        ),
    ]
