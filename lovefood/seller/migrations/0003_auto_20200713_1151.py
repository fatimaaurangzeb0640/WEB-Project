# Generated by Django 3.0.5 on 2020-07-13 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='customizable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dish',
            name='glutten_free',
            field=models.BooleanField(default=False),
        ),
    ]