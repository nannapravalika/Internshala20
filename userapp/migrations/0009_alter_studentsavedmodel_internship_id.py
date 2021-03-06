# Generated by Django 4.0.1 on 2022-03-28 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employerapp', '0003_employepostmodel_mobile'),
        ('userapp', '0008_alter_studentsavedmodel_internship_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsavedmodel',
            name='internship_id',
            field=models.ForeignKey(db_column='internship_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intern', to='employerapp.employepostmodel'),
        ),
    ]
