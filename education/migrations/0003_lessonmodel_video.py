# Generated by Django 4.0.6 on 2022-07-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_lessonmodel_photo_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonmodel',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/%Y/%m/%d/'),
        ),
    ]
