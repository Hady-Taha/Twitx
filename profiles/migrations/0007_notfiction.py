# Generated by Django 3.1.5 on 2021-02-15 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_profile_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notfiction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clear', models.BooleanField(default=False)),
                ('note', models.ManyToManyField(blank=True, null=True, to='profiles.RelationShip')),
            ],
        ),
    ]
