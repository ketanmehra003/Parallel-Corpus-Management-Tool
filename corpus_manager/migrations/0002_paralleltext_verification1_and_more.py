# Generated by Django 5.0.2 on 2024-02-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpus_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paralleltext',
            name='verification1',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paralleltext',
            name='verification2',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paralleltext',
            name='verification3',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paralleltext',
            name='verification4',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paralleltext',
            name='verification5',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
            preserve_default=False,
        ),
    ]