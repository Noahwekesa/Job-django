# Generated by Django 4.1.7 on 2023-10-21 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_rename_status_applyjob_job_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applyjob',
            name='experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applyjob',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applyjob', to='job.job'),
        ),
    ]
