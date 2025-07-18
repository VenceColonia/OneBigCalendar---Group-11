# Generated by Django 5.2.4 on 2025-07-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eventcard",
            name="category",
        ),
        migrations.AddField(
            model_name="eventcard",
            name="tag",
            field=models.CharField(
                choices=[("LIONS", "LIONS Events"), ("COA", "COA Events")],
                default="LIONS",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="eventcard",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
