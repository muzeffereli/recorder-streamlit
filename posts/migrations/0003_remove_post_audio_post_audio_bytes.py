# Generated by Django 4.1.2 on 2022-10-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_post_audio"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="audio",
        ),
        migrations.AddField(
            model_name="post",
            name="audio_bytes",
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
