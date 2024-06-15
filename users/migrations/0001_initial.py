# Generated by Django 5.0.6 on 2024-06-15 11:01

import django.contrib.auth.validators
import django.utils.timezone
import users.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('last_name', models.CharField(max_length=150, verbose_name='姓')),
                ('first_name', models.CharField(max_length=150, verbose_name='名')),
                ('last_name_kana', models.CharField(max_length=150, verbose_name='姓（かな）')),
                ('first_name_kana', models.CharField(max_length=150, verbose_name='名（かな）')),
                ('old_last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='旧姓')),
                ('old_last_name_kana', models.CharField(blank=True, max_length=150, null=True, verbose_name='旧姓（かな）')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='メールアドレス')),
                ('sex', models.CharField(choices=[('男性', '男性'), ('女性', '女性')], max_length=4, verbose_name='性別')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生年月日')),
                ('country', models.CharField(default='日本', editable=False, max_length=15, verbose_name='国')),
                ('postal_code', models.CharField(blank=True, max_length=7, null=True, verbose_name='郵便番号（ハイフンなし）')),
                ('prefecture', models.CharField(blank=True, max_length=5, null=True, verbose_name='都道府県')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='市区町村番地')),
                ('building', models.CharField(blank=True, max_length=30, null=True, verbose_name='建物名')),
                ('tel', models.CharField(blank=True, max_length=11, null=True, verbose_name='電話番号（ハイフンなし）')),
                ('url', models.URLField(blank=True, max_length=300, null=True, verbose_name='URL')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'ユーザー',
                'db_table': 'User',
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
