# Generated by Django 2.0 on 2018-01-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0006_auto_20180106_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=200)),
                ('album_year', models.IntegerField()),
                ('album_text', models.CharField(max_length=1000)),
                ('album_image_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Art',
        ),
    ]
