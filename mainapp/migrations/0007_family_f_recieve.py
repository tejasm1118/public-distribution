# Generated by Django 2.0.6 on 2018-09-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_item_i_fam'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='f_recieve',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10),
        ),
    ]
