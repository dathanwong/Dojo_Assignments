# Generated by Django 2.2.4 on 2020-05-20 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirmPassword',
        ),
    ]
