# Generated by Django 3.0.8 on 2022-01-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211230_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'testest',
            },
        ),
        # migrations.RenameField(
        #     model_name='image',
        #     old_name='memo_id',
        #     new_name='memo',
        # ),
        # migrations.RenameField(
        #     model_name='link',
        #     old_name='memo_id',
        #     new_name='memo',
        # ),
        # migrations.RenameField(
        #     model_name='memo',
        #     old_name='tag_id',
        #     new_name='tag',
        # ),
        # migrations.RenameField(
        #     model_name='schedule',
        #     old_name='memo_id',
        #     new_name='memo',
        # ),
        # migrations.RenameField(
        #     model_name='tag',
        #     old_name='user_id',
        #     new_name='user',
        # ),
        migrations.AlterField(
            model_name='memo',
            name='memo_text',
            field=models.TextField(null=True),
        ),
    ]