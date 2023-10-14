# Generated by Django 4.1.7 on 2023-10-14 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_alter_resume_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(choices=[('null', 'not specified'), ('Male', 'Male'), ('Female', 'Female')], default='null', max_length=50),
        ),
    ]
