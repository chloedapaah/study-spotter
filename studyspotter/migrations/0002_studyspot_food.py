# Generated by Django 4.2.6 on 2023-11-13 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyspotter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyspot',
            name='food',
            field=models.BooleanField(default=False),
        ),
    ]
