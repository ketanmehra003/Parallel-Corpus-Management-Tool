# Generated by Django 5.0.2 on 2024-02-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpus_manager', '0004_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paralleltext',
            name='target_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paralleltext',
            name='verification1',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AlterField(
            model_name='paralleltext',
            name='verification2',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AlterField(
            model_name='paralleltext',
            name='verification3',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AlterField(
            model_name='paralleltext',
            name='verification4',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AlterField(
            model_name='paralleltext',
            name='verification5',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
    ]
