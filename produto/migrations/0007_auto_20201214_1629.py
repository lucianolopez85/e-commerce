# Generated by Django 3.1.3 on 2020-12-14 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_categoria'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='variacao',
            name='produto',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.DeleteModel(
            name='Variacao',
        ),
    ]