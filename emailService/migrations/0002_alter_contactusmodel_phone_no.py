# Generated by Django 4.1.1 on 2022-10-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailService', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='phone_no',
            field=models.CharField(max_length=50),
        ),
    ]
