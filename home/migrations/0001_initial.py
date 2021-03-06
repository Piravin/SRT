# Generated by Django 3.0.7 on 2020-06-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=12)),
                ('twitter', models.CharField(max_length=1000)),
                ('facebook', models.CharField(max_length=1000)),
                ('instagram', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, default='logo.png', upload_to='logo')),
                ('quote1', models.CharField(default='SASTRA Racing Team - Baja', max_length=50)),
                ('quote2', models.CharField(blank=True, default='Quotes comming soon..', max_length=100)),
                ('backgroundimage1', models.ImageField(blank=True, default='back1.jpg', upload_to='back1')),
                ('backgroundimage2', models.ImageField(blank=True, default='back2.jpg', upload_to='back2')),
                ('backgroundimage3', models.ImageField(blank=True, default='default.png', upload_to='back3')),
                ('video', models.CharField(blank=True, max_length=1000)),
                ('video_description', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('contacts', models.TextField(blank=True)),
                ('team_background', models.ImageField(blank=True, default='back2.jpg', upload_to='team')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(blank=True)),
                ('subject', models.TextField(blank=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slide_link', models.CharField(blank=True, default='#', max_length=1000)),
                ('slide', models.ImageField(upload_to='slides')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sponsor', models.ImageField(upload_to='sponsors')),
                ('sponsor_link', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
