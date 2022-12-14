# Generated by Django 4.1.3 on 2022-11-16 14:11

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="post", managers=[("object", django.db.models.manager.Manager()),],
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="publish"),
        ),
    ]
