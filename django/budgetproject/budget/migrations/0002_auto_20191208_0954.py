# Generated by Django 3.0 on 2019-12-08 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='memo',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='budget.Project'),
        ),
    ]
