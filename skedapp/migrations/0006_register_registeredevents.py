# Generated by Django 3.2.3 on 2021-05-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skedapp', '0005_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='registeredevents',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]