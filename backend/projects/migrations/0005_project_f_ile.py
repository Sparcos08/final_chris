# Generated by Django 4.1.5 on 2023-03-03 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_members_id_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='f_ile',
            field=models.FileField(null=True, upload_to='store/files/'),
        ),
    ]
