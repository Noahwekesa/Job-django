# Generated by Django 4.1.7 on 2023-10-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_skills_alter_resume_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
    ]
