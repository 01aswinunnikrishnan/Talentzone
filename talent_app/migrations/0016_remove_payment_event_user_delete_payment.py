# Generated by Django 4.1.7 on 2023-04-05 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talent_app', '0015_payment_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_event',
            name='user',
        ),
        migrations.DeleteModel(
            name='payment',
        ),
    ]
