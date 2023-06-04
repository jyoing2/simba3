# Generated by Django 4.2.1 on 2023-06-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Keyword",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("keyword", models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name="post",
            old_name="write",
            new_name="writer",
        ),
        migrations.AddField(
            model_name="post",
            name="categorys",
            field=models.ManyToManyField(related_name="cats", to="post.category"),
        ),
        migrations.AddField(
            model_name="post",
            name="keywords",
            field=models.ManyToManyField(related_name="keys", to="post.keyword"),
        ),
    ]
