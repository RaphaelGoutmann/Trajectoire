# Generated by Django 4.1.4 on 2023-11-05 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='author',
        ),
    ]
