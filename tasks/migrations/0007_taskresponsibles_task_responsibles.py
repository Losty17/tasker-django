# Generated by Django 5.1.3 on 2024-12-01 23:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_categories_alter_taskcategories_category_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskResponsibles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='responsibles',
            field=models.ManyToManyField(related_name='tasks', through='tasks.TaskResponsibles', to=settings.AUTH_USER_MODEL),
        ),
    ]
