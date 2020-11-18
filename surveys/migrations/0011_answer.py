# Generated by Django 3.1.3 on 2020-11-18 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('surveys', '0010_auto_20201118_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE,
                                                  related_name='question', to='surveys.question')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                           related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
