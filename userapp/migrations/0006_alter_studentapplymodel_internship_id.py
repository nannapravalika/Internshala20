# Generated by Django 4.0.1 on 2022-03-28 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employerapp', '0003_employepostmodel_mobile'),
        ('userapp', '0005_remove_studentapplymodel_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentapplymodel',
            name='internship_id',
            field=models.ForeignKey(db_column='internship_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='employerapp.employepostmodel'),
        ),
    ]
