# Generated by Django 3.2.9 on 2021-12-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_remove_registeruser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='NA', max_length=11),
            preserve_default=False,
        ),
    ]
