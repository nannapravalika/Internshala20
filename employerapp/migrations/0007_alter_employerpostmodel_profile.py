# Generated by Django 4.0.1 on 2022-02-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employerapp', '0006_alter_employerpostmodel_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employerpostmodel',
            name='Profile',
            field=models.CharField(help_text='Profile', max_length=100),
        ),
    ]