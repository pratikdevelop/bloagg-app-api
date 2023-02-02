# Generated by Django 4.1.5 on 2023-01-22 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_blogs_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=266)),
                ('createdAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='post',
        ),
        migrations.AddField(
            model_name='blogs',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]