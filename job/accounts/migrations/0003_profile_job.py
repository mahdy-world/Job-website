# Generated by Django 3.2.3 on 2021-07-25 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210719_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(default=1, max_length=50, verbose_name='job'),
            preserve_default=False,
        ),
    ]
