# Generated by Django 3.2.3 on 2021-05-24 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skedapp', '0006_register_registeredevents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='ename',
        ),
    ]
