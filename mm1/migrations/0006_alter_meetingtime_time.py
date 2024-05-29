# Generated by Django 4.2.5 on 2024-05-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm1', '0005_alter_meetingtime_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingtime',
            name='time',
            field=models.CharField(choices=[('8:00 - 8:55', '8:00 - 8:55'), ('8:55 - 9:50', '8:55 - 9:50'), ('10:00 - 11:55', '10:00 - 11:55'), ('3:05 - 4:00', '3:05 - 4:00'), ('2:10 - 4:00', '2:10 - 4:00'), ('4:10 - 5:05', '4:10 - 5:05'), ('5:05 - 6:00', '5:05 - 6:00')], default='08:00 - 08:55', max_length=50),
        ),
    ]
