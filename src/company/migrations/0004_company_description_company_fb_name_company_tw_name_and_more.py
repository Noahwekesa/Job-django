# Generated by Django 4.1.7 on 2023-10-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='fb_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='tw_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]