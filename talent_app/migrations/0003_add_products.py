# Generated by Django 4.1.7 on 2023-03-25 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('talent_app', '0002_organisation_register_artist_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=100, null=True)),
                ('rate', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('product_image', models.ImageField(null=True, upload_to='media/')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_app.artist_register')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
