# Generated by Django 3.2.16 on 2022-12-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0004_employee_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='location',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
