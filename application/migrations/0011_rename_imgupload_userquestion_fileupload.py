# Generated by Django 3.2.9 on 2021-12-19 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_userquestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userquestion',
            old_name='imgupload',
            new_name='fileupload',
        ),
    ]
