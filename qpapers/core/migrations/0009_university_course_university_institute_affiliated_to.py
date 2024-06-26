# Generated by Django 5.0.4 on 2024-05-06 12:57

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_year_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uni_id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz1234567890', length=10, max_length=20, prefix='uni-', unique=True)),
                ('uni_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Universities',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.university'),
        ),
        migrations.AddField(
            model_name='institute',
            name='affiliated_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.university'),
        ),
    ]
