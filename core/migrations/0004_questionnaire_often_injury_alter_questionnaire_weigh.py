# Generated by Django 4.2.1 on 2023-08-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_questionnaire_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='often_injury',
            field=models.CharField(choices=[('OM', 'one on mounth'), ('OY', 'one on year'), ('O5', 'one on 5 years'), ('NI', "i don't have injury")], default='NI', max_length=255),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='weigh',
            field=models.DecimalField(decimal_places=1, default=60, max_digits=4),
        ),
    ]
