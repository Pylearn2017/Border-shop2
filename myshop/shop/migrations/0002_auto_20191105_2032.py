# Generated by Django 2.0.5 on 2019-11-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='age',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='number_of_players',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
