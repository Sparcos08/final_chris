# Generated by Django 4.1.5 on 2023-03-04 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_f_ile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='f_ile',
            new_name='uploaded_file',
        ),
    ]
