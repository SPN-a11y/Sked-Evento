# Generated by Django 3.2.3 on 2021-05-24 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skedapp', '0007_remove_register_ename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='phoneno',
        ),
    ]
