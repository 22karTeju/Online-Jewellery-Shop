# Generated by Django 5.0 on 2023-12-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Japp', '0004_alter_cart_pid_alter_cart_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
