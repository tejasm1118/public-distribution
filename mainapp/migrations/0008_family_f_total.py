# Generated by Django 2.0.6 on 2018-09-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_family_f_recieve'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='f_total',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
