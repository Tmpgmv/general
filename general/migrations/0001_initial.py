# Generated by Django 3.2.3 on 2021-05-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('key', models.CharField(default='general_settings', max_length=16, primary_key=True, serialize=False)),
                ('template_debugging', models.BooleanField(default=False, verbose_name='Template debugging')),
            ],
            options={
                'verbose_name': 'General sertings',
                'verbose_name_plural': 'General sertings',
            },
        ),
    ]
