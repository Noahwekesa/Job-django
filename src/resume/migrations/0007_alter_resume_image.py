# Generated by Django 4.1.7 on 2023-10-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_resume_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='resume/'),
        ),
    ]
