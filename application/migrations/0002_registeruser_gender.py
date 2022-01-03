# Generated by Django 3.2.9 on 2021-12-06 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='not defined', max_length=11),
            preserve_default=False,
        ),
    ]
