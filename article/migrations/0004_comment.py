# Generated by Django 2.2.7 on 2019-12-19 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20191212_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=30, verbose_name='Ad')),
                ('comment_content', models.CharField(max_length=100, verbose_name='Şərh')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article', verbose_name='Meqale')),
            ],
        ),
    ]
