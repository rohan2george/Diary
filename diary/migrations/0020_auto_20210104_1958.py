# Generated by Django 3.0.8 on 2021-01-05 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0019_remove_remind_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='remindtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Remind',
        ),
    ]
