# Generated by Django 3.0.2 on 2020-01-11 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20200111_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='replyTo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='post.Comment'),
        ),
    ]
