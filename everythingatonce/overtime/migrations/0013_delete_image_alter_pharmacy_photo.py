# Generated by Django 5.0.1 on 2024-02-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overtime', '0012_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='photo',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
