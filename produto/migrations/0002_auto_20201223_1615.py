# Generated by Django 3.1.4 on 2020-12-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='vezes_sem_juros',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
