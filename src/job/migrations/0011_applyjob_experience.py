# Generated by Django 4.1.7 on 2023-10-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_alter_applyjob_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='experience',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]