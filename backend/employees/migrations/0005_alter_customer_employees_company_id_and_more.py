# Generated by Django 4.1.5 on 2023-02-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_alter_customer_employees_company_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_employees',
            name='company_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier_employees',
            name='company_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]