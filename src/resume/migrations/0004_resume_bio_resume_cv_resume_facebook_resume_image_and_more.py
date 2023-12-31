# Generated by Django 4.1.7 on 2023-10-06 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_rename_loaction_resume_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='resume/'),
        ),
        migrations.AddField(
            model_name='resume',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='resume/'),
        ),
        migrations.AddField(
            model_name='resume',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
