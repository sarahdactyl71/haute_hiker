# Generated by Django 2.2 on 2019-06-03 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20190426_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=500)),
                ('image_title', models.CharField(max_length=50)),
                ('created', models.DateTimeField(verbose_name='date created')),
                ('updated', models.DateTimeField(verbose_name='date updated')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Article')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Review')),
            ],
        ),
    ]
