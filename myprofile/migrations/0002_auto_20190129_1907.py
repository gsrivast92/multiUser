# Generated by Django 2.1.5 on 2019-01-29 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='userKey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]