# Generated by Django 5.0 on 2023-12-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('Metal_Type', models.CharField(max_length=100)),
                ('Weight_gm', models.FloatField()),
                ('Cat', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
