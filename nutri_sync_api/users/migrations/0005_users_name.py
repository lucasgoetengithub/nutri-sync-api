# Generated by Django 5.0.1 on 2024-02-01 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(default='TESTE', max_length=150),
            preserve_default=False,
        ),
    ]