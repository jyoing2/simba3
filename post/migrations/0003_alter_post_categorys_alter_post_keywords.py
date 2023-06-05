# Generated by Django 4.2.1 on 2023-06-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_category_keyword_rename_write_post_writer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorys',
            field=models.ManyToManyField(related_name='categorys', to='post.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=models.ManyToManyField(related_name='keywords', to='post.keyword'),
        ),
    ]
