# Generated by Django 4.1.7 on 2023-04-18 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talent_app', '0021_payment_event_organisation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_event',
            name='organisation',
        ),
    ]