# Generated by Django 5.0.1 on 2024-02-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overtime', '0002_alter_overtimes_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='overtimes',
            name='districts',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
