# Generated by Django 4.1.4 on 2023-01-06 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author_temp',
            new_name='author',
        ),
    ]
