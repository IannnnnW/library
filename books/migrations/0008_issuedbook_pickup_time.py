# Generated by Django 4.0.5 on 2022-07-04 13:11

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_issuedbook_borrower'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbook',
            name='pickup_time',
            field=models.DateTimeField(default=books.models.book_time_limit),
        ),
    ]
