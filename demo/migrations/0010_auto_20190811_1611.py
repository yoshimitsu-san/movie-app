# Generated by Django 2.2.3 on 2019-08-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('demo', '0009_auto_20190811_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auhtor',
            name='books',
            field=models.ManyToManyField(
                related_name='auhtors', to='demo.Book'),
        ),
    ]