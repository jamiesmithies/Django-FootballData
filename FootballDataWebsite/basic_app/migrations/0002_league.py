# Generated by Django 3.0.3 on 2020-08-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('team_name', models.CharField(max_length=30)),
                ('points', models.IntegerField()),
            ],
        ),
    ]
