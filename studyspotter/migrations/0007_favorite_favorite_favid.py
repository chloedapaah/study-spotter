# Generated by Django 4.2.6 on 2023-12-04 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studyspotter', '0006_alter_studyspot_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('pin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyspotter.studyspot')),
            ],
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('pin', 'user'), name='favid'),
        ),
    ]
