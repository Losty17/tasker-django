# Generated by Django 5.1.3 on 2024-11-30 22:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('tasks', '0004_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcategories',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='taskcategories',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='tasks.task'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
