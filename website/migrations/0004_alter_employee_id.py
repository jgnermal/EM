# Generated by Django 5.1.1 on 2024-11-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_employee_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
