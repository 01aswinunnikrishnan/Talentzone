# Generated by Django 4.1.7 on 2023-04-18 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent_app', '0022_remove_payment_event_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_event',
            name='organisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_app.organisation_register'),
        ),
    ]