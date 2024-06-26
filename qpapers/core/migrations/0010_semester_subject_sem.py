# Generated by Django 5.0.4 on 2024-05-06 16:26

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_university_course_university_institute_affiliated_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem_id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz1234567890', length=10, max_length=20, prefix='sem-', unique=True)),
                ('sem', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Years',
            },
        ),
        migrations.AddField(
            model_name='subject',
            name='sem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.semester'),
        ),
    ]
