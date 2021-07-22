# Generated by Django 3.0.5 on 2020-05-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_clientprofile_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='contact1email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='contact2email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]