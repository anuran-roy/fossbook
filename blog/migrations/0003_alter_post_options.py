# Generated by Django 3.2.5 on 2021-07-31 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210731_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on', '-updated_on', '-author', '-title']},
        ),
    ]
