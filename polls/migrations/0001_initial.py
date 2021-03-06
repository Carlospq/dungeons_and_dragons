# Generated by Django 3.0.5 on 2021-01-30 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability_score_increase', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('alignment', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('speed', models.IntegerField(default=20)),
                ('languages', models.CharField(max_length=200)),
                ('subraces', models.CharField(max_length=100)),
                ('darkvision', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=100)),
                ('subrace_ability_score_increase', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
        ),
    ]
