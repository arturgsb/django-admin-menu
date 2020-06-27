# Generated by Django 3.0 on 2020-06-27 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='continent',
            name='code',
            field=models.CharField(default='EU', help_text='Two letter continent code', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='world.Continent'),
        ),
    ]
