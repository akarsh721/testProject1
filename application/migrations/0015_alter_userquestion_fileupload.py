# Generated by Django 3.2.9 on 2022-01-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_alter_userquestion_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquestion',
            name='fileupload',
            field=models.FileField(blank=True, null=True, upload_to='UploadedFile'),
        ),
    ]
