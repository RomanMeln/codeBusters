# Generated by Django 4.1.1 on 2022-10-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0006_merge_20221027_1027"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="post_image",
                verbose_name="Главное изображение статьи",
            ),
        ),
    ]
