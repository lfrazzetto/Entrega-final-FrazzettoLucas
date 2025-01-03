# Generated by Django 5.1.4 on 2024-12-06 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blog_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='content',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='default.png', upload_to='blog_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(default='default.png', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
