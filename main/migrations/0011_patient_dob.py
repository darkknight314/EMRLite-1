# Generated by Django 2.2.2 on 2019-07-08 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_merge_20190707_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
