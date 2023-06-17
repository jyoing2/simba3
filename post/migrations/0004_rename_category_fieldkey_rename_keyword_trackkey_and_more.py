# Generated by Django 4.2.1 on 2023-06-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0003_alter_post_categorys_alter_post_keywords"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Category",
            new_name="FieldKey",
        ),
        migrations.RenameModel(
            old_name="Keyword",
            new_name="TrackKey",
        ),
        migrations.RenameField(
            model_name="fieldkey",
            old_name="category",
            new_name="fieldKey",
        ),
        migrations.RenameField(
            model_name="trackkey",
            old_name="keyword",
            new_name="trackKey",
        ),
        migrations.RemoveField(
            model_name="post",
            name="categorys",
        ),
        migrations.RemoveField(
            model_name="post",
            name="keywords",
        ),
        migrations.AddField(
            model_name="post",
            name="fieldKey",
            field=models.ManyToManyField(
                default="", related_name="field_Key", to="post.fieldkey"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="link",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="post",
            name="recruit_date",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="post",
            name="team_name",
            field=models.CharField(default="", max_length=30),
        ),
        migrations.AddField(
            model_name="post",
            name="trackKey",
            field=models.ManyToManyField(
                default="", related_name="track_Key", to="post.trackkey"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="about_us",
            field=models.TextField(default=""),
        ),
    ]