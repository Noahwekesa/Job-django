# Generated by Django 4.1.7 on 2023-10-21 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_applyjob_content_applyjob_experience_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applyjob',
            name='content',
        ),
        migrations.RemoveField(
            model_name='applyjob',
            name='experience',
        ),
    ]
