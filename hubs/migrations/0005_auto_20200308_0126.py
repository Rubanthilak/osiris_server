# Generated by Django 2.2.10 on 2020-03-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0004_auto_20200308_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='hub_id',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]