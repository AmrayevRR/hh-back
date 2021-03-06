# Generated by Django 2.1.5 on 2021-04-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_company_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='description',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.FloatField(null=True),
        ),
    ]
