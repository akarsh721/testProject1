# Generated by Django 3.2.9 on 2021-12-22 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_rename_imgupload_userquestion_fileupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='queriedBy',
            field=models.CharField(default='NA', max_length=30),
            preserve_default=False,
        ),
    ]
