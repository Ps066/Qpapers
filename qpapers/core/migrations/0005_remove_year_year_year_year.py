# Generated by Django 5.0.4 on 2024-05-05 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_year_questions_year_subject_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='year',
            name='Year',
        ),
        migrations.AddField(
            model_name='year',
            name='year',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
