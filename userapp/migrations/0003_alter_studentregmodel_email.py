# Generated by Django 4.0.1 on 2022-02-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_studentregmodel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregmodel',
            name='email',
            field=models.EmailField(help_text='Enter email', max_length=100),
        ),
    ]