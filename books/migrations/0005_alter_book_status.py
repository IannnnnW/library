# Generated by Django 4.0.5 on 2022-06-25 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_rename_name_book_title_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.BooleanField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')]),
        ),
    ]