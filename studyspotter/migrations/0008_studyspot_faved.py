# Generated by Django 4.2.6 on 2023-12-04 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyspotter', '0007_favorite_favorite_favid'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyspot',
            name='faved',
            field=models.BooleanField(default=False),
        ),
    ]
