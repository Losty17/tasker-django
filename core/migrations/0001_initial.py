# Generated by Django 5.1.3 on 2024-12-01 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0006_task_categories_alter_taskcategories_category_and_more"),
    ]

    def insert_data(apps, schema_editor):
        User = apps.get_model("auth", "User")
        User.objects.create_user(
            username="johndoe", password="123456", first_name="John Doe"
        )
        User.objects.create_user(
            username="janedoe", password="123456", first_name="Jane Doe"
        )
        User.objects.create_user(
            username="alice", password="123456", first_name="Alice"
        )
        User.objects.create_user(username="bob", password="123456", first_name="Bob")

    operations = [
        migrations.RunPython(insert_data),
    ]
