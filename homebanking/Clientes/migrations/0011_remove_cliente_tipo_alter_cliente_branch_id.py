# Generated by Django 4.1 on 2022-08-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0010_alter_cliente_branch_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='branch_id',
            field=models.IntegerField(),
        ),
    ]