# Generated by Django 3.2.9 on 2021-12-17 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_registeruser_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeruser',
            name='contact',
        ),
    ]
