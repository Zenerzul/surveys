# Generated by Django 3.1.3 on 2020-11-18 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0007_auto_20201118_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='question',
        ),
        migrations.AddField(
            model_name='survey',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='questions', to='surveys.question'),
        ),
    ]
