# Generated by Django 4.0.6 on 2022-07-30 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='related_model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='album.album'),
            preserve_default=False,
        ),
    ]
