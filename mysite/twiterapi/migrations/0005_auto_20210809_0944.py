# Generated by Django 3.2.6 on 2021-08-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twiterapi', '0004_auto_20210809_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='mention',
            name='avatarUrl',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='mention',
            name='description',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='mention',
            name='followers',
            field=models.IntegerField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='mention',
            name='following',
            field=models.IntegerField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='mention',
            name='name',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]
