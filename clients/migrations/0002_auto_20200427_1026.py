# Generated by Django 3.0.5 on 2020-04-27 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='contact1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='contact2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
