# Generated by Django 4.1.7 on 2024-01-17 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_alter_conversationmessage_applyjob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='content',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='city',
            field=models.CharField(blank=True, choices=[('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Kiambu', 'Kiambu'), ('Nakuru', 'Nakuru')], max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='industry',
            field=models.CharField(blank=True, choices=[('Construction', 'Construction'), ('Health Services', 'Health Services'), ('Finance', 'Finance'), ('Information Technology', 'Information Technology')], max_length=24, null=True),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Industry',
        ),
    ]