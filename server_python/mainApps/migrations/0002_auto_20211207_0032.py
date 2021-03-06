# Generated by Django 3.2.6 on 2021-12-06 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructions',
            options={'verbose_name': 'Инструкции', 'verbose_name_plural': 'Инструкция'},
        ),
        migrations.AlterModelOptions(
            name='office',
            options={'verbose_name': 'Подразделения', 'verbose_name_plural': 'Подразделение'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Сотрудники', 'verbose_name_plural': 'Сотрудник'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'Должности', 'verbose_name_plural': 'Должность'},
        ),
        migrations.AlterField(
            model_name='office',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=60, null=True, verbose_name='Название подразделения'),
        ),
    ]
