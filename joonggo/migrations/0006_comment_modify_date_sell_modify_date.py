# Generated by Django 4.1.7 on 2023-03-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("joonggo", "0005_alter_sell_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sell",
            name="modify_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
