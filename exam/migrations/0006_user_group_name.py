# Generated by Django 4.0.6 on 2022-07-20 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_rename_file_path_question_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
