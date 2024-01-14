# Generated by Django 4.1.7 on 2024-01-14 09:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('total_question', models.IntegerField(blank=True, default=0, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.science')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='recourse',
            name='group',
        ),
        migrations.RemoveField(
            model_name='recourse',
            name='science',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='group',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='science',
        ),
        migrations.RemoveField(
            model_name='video',
            name='group',
        ),
        migrations.RemoveField(
            model_name='video',
            name='science',
        ),
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
        migrations.RemoveField(
            model_name='test',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='test',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='test',
            name='required',
        ),
        migrations.AlterField(
            model_name='test',
            name='number',
            field=models.IntegerField(default=10, verbose_name='Nechta savol berilishi kerak'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Recourse',
        ),
        migrations.DeleteModel(
            name='Slide',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
