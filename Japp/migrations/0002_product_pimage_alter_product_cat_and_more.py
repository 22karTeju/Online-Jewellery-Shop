# Generated by Django 5.0 on 2023-12-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Japp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='Cat',
            field=models.IntegerField(choices=[(1, 'Gold'), (2, 'Silver'), (3, 'Dimond')], verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Metal_Type',
            field=models.CharField(max_length=100, verbose_name='Metal Type'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Weight_gm',
            field=models.FloatField(verbose_name='Metal_Weight gm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Available'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Product Name'),
        ),
    ]
