# Generated by Django 4.2.8 on 2024-01-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0005_alter_post_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(
                choices=[("Web Development", "WB"), ("Data Science", "DS")],
                default="Wb",
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]
