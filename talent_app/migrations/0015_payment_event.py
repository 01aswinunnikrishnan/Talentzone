# Generated by Django 4.1.7 on 2023-04-05 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent_app', '0014_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(max_length=100, null=True)),
                ('cardno', models.CharField(max_length=100, null=True)),
                ('expiry', models.CharField(max_length=100, null=True)),
                ('cvv', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_app.artist_register')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_app.user_register')),
            ],
        ),
    ]
