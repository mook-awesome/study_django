# Generated by Django 5.0 on 2023-12-15 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0007_alter_review_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_user',
        ),
    ]
