# Generated by Django 2.0 on 2018-01-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(max_length=200)),
                ('work_date', models.CharField(max_length=200)),
                ('work_text', models.CharField(max_length=2000)),
            ],
        ),
    ]