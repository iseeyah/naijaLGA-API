# Generated by Django 2.0 on 2018-07-20 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0004_lga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lga',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lga', to='state.State'),
        ),
    ]