# Generated by Django 3.0.5 on 2021-02-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pjs', '0003_auto_20210201_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='desc',
        ),
        migrations.AddField(
            model_name='class',
            name='descr',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
