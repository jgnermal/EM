# Generated by Django 5.1.1 on 2024-11-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_employee_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.CharField(max_length=100),
        ),
    ]