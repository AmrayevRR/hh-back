# Generated by Django 2.1.5 on 2021-04-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210412_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.FloatField(),
        ),
    ]