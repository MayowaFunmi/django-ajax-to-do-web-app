# Generated by Django 3.0.7 on 2020-08-02 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['completed', 'date']},
        ),
    ]