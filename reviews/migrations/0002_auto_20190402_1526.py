# Generated by Django 2.2 on 2019-04-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='brand',
            field=models.CharField(default='great', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='product_name',
            field=models.CharField(default='great', max_length=30),
            preserve_default=False,
        ),
    ]
