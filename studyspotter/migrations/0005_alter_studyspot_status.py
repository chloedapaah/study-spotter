# Generated by Django 4.2.6 on 2023-11-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyspotter', '0004_merge_20231113_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyspot',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=15),
        ),
    ]
