# Generated by Django 5.0.4 on 2024-05-05 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_code',
            field=models.CharField(default=1, max_length=25, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_code',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
