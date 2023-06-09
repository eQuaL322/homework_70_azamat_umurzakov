# Generated by Django 4.1.7 on 2023-03-21 00:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(limit_value=3)], verbose_name='Название')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('users', models.ManyToManyField(blank=True, null=True, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тип')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(limit_value=3)], verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='Полное описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='issue_tracker.project', verbose_name='Проект')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='issue_tracker.status')),
                ('types', models.ManyToManyField(related_name='tasks', to='issue_tracker.type')),
            ],
        ),
    ]
