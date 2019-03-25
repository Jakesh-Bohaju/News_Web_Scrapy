# Generated by Django 2.1.7 on 2019-03-24 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TheodoTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=150)),
                ('fun_fact', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'theodo UK team',
            },
        ),
    ]
