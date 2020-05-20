# Generated by Django 3.0.6 on 2020-05-20 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length='1000', verbose_name='Content')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentArticle', to='news.Article', verbose_name='Article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentAuthor', to='news.Author', verbose_name='Author')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
