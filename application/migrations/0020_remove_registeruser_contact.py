# Generated by Django 3.2.9 on 2022-02-03 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0019_alter_registeruser_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeruser',
            name='contact',
        ),
    ]