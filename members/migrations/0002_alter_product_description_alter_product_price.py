# Generated by Django 4.2.4 on 2023-08-31 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
