# Generated by Django 3.2.11 on 2022-01-14 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topicandcomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=70)),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='myapp.topic')),
            ],
        ),
    ]
