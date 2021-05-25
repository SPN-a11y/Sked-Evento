# Generated by Django 3.2.3 on 2021-05-22 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skedapp', '0002_auto_20210522_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('edate', models.CharField(max_length=100)),
                ('etime', models.CharField(max_length=100)),
                ('eloc', models.CharField(max_length=100)),
                ('enum', models.CharField(max_length=100)),
                ('edisc', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='event',
        ),
    ]
