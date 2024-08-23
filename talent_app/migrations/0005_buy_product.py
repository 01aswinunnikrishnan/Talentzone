# Generated by Django 4.1.7 on 2023-03-28 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent_app', '0004_remove_add_products_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardname', models.CharField(max_length=100, null=True)),
                ('cardno', models.CharField(max_length=100, null=True)),
                ('expiry', models.CharField(max_length=100, null=True)),
                ('cvv', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='talent_app.user_register')),
            ],
        ),
    ]