# Generated by Django 3.1.6 on 2021-02-25 23:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20210224_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_level', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(5)])),
                ('rating_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.artist')),
                ('rating_artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.artwork')),
            ],
        ),
    ]