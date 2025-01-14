# Generated by Django 4.1.7 on 2023-03-28 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent_app', '0005_buy_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100, null=True)),
                ('venue', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('date', models.CharField(max_length=100, null=True)),
                ('time', models.CharField(max_length=100, null=True)),
                ('organisation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_app.organisation_register')),
            ],
        ),
    ]
