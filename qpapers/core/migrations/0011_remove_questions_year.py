# Generated by Django 5.0.4 on 2024-05-06 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_semester_subject_sem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='year',
        ),
    ]