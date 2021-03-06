# Generated by Django 4.0.1 on 2022-02-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployePostModel',
            fields=[
                ('emp_id', models.IntegerField(null=True)),
                ('internship_id', models.AutoField(primary_key=True, serialize=False)),
                ('Organization_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('Profile', models.CharField(max_length=100)),
                ('Internship_type', models.CharField(max_length=100)),
                ('No_of_openings', models.IntegerField()),
                ('Start_Date', models.CharField(max_length=100)),
                ('Duration', models.CharField(max_length=100)),
                ('Stiepend', models.CharField(max_length=100, null=True)),
                ('Skills', models.TextField()),
                ('Description', models.TextField()),
                ('Profile_picture', models.ImageField(null=True, upload_to='images/')),
                ('Posted_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('Pan', models.CharField(max_length=100, null=True)),
                ('Year_of_establishment', models.IntegerField(null=True)),
                ('Published_date', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'post_details',
            },
        ),
        migrations.CreateModel(
            name='EmployerRegModel',
            fields=[
                ('employer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='Enter First name', max_length=100)),
                ('last_name', models.CharField(help_text='Enter Last name', max_length=100)),
                ('email', models.EmailField(help_text='Enter First name', max_length=100)),
                ('password', models.CharField(help_text='Enter Password', max_length=100)),
            ],
            options={
                'db_table': 'employer_details',
            },
        ),
    ]
