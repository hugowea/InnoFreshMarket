# Generated by Django 4.2.11 on 2024-04-26 00:35

import back.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('role', models.CharField(choices=[('FM', 'Фермер'), ('BY', 'Покупатель'), ('AD', 'Админ')], default='BY', max_length=3, verbose_name='Роль')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('card', models.CharField(blank=True, max_length=20, null=True)),
                ('numbers_of_comments', models.IntegerField(default=0)),
                ('rate', models.FloatField(default=0.0)),
                ('balance', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', back.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, null=True, verbose_name='Время отправки')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Отправитель')),
                ('rate', models.IntegerField(verbose_name='Оценка')),
                ('text', models.CharField(max_length=2048, null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='Название')),
                ('cost_retail', models.FloatField(verbose_name='Розничная цена')),
                ('cost_wholesale', models.FloatField(blank=True, null=True, verbose_name='Оптовая цена')),
                ('doc', models.FileField(upload_to='uploads/', verbose_name='Фото')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата готовности')),
                ('number', models.FloatField(verbose_name='Количество товара')),
                ('number_wholesale', models.FloatField(blank=True, null=True, verbose_name='Мин. кол-во товара для оптовой закупки')),
                ('description', models.CharField(max_length=63, verbose_name='Описание')),
                ('expire_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания срока годности')),
                ('number_for_month', models.FloatField(blank=True, null=True, verbose_name='Количество товара на месяц(подписка)')),
                ('subscriptable', models.BooleanField(verbose_name='Возможность подписки')),
                ('category', models.CharField(choices=[('FR', 'Фрукты'), ('VE', 'Овощи'), ('OT', 'Другие')], default='OT', max_length=2, verbose_name='Категории')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name='Количество товара')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to=settings.AUTH_USER_MODEL, verbose_name='Фермер')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.item', verbose_name='Покупка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Часть заказа',
                'verbose_name_plural': 'Части заказа',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Статус покупки')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата покупки')),
                ('payment', models.CharField(blank=True, choices=[('CA', 'Карта'), ('BC', 'Юр. лицо'), ('CS', 'Наличные')], default='BY', max_length=3, null=True, verbose_name='Роль')),
                ('shipping_address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адрес доставки')),
                ('way_of_shipping', models.CharField(blank=True, choices=[('CA', 'Карта'), ('BC', 'Юр. лицо'), ('CS', 'Наличные')], default='BY', max_length=3, null=True, verbose_name='Роль')),
                ('date_of_receive', models.DateField(blank=True, null=True, verbose_name='Дата получения заказа')),
                ('total_price', models.FloatField(default=0, verbose_name='Общая стоимость')),
                ('items', models.ManyToManyField(blank=True, related_name='items_name_123', to='accounts.orderitems', verbose_name='Товары')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2048, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата отправки')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Отправитель')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=255, null=True, verbose_name='Название чата1')),
                ('name2', models.CharField(max_length=255, null=True, verbose_name='Название чата2')),
                ('messages', models.ManyToManyField(blank=True, related_name='messages', to='accounts.message', verbose_name='Сообщения')),
                ('user1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель1')),
                ('user2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель2')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='chats',
            field=models.ManyToManyField(blank=True, related_name='chats', to='accounts.chat', verbose_name='Чаты'),
        ),
        migrations.AddField(
            model_name='user',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='accounts.comment', verbose_name='Комментарии'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
