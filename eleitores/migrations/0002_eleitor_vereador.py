# Generated by Django 4.2.5 on 2024-10-30 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vereadores', '0001_initial'),
        ('eleitores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleitor',
            name='vereador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='eleitores', to='vereadores.vereador'),
            preserve_default=False,
        ),
    ]
