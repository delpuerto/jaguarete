# Generated by Django 3.2.4 on 2021-06-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaguareteAPP', '0003_categoria_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
