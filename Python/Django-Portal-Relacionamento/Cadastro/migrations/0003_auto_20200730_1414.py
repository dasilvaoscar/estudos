# Generated by Django 2.2.4 on 2020-07-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0002_auto_20200724_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='anexos',
            name='tipo',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='anexos',
            name='arquivo',
            field=models.FileField(blank=True, upload_to='media/', verbose_name='Novos Arquivos'),
        ),
    ]
