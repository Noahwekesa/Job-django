# Generated by Django 4.1.7 on 2023-10-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_alter_resume_skills_delete_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='resume',
            name='bio',
        ),
        migrations.AddField(
            model_name='resume',
            name='bio',
            field=models.ManyToManyField(to='resume.skill'),
        ),
    ]
