# Generated by Django 5.0.4 on 2024-05-05 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_course_course_code_alter_subject_sub_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='rbt',
            name='rbt_value',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rbt',
            name='rbt_level',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
