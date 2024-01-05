# budget_calculator_api
Это код моего бота в ТГ. Его основная функция - удобный учет ежедневных расходов. 
Проверить его работу можно по адресу: 
https://t.me/test_your_potential_bot

# Инструкция по развёртыванию бота
#### 1) Создние .env файлов
- /bot
```shell
TOKEN="<YOUR TELEGRAM TOKEN>"
URL='api:8000'
PASSWORD="api_default_password"
```
- /compose
```shell
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)a
DB_PORT=5432 # порт для подключения к БД
```
#### 2) Развёртывание контейнеров
- в терминале перейти в папку .../budget_calculator_api/compose
- запуск контейнеров командой:
```shell
sudo docker compose up -d
```
- проверить, что контейнеры запущены командой:
```shell
sudo docker ps -a
```


# Как это всё работает
## 1. Общая информация по составным частям
Каждая часть работает в отдельном контейнере
### 1.1. Bot
Написан на python
- Непосредственно взаимодействует с пользователем
- Обрабатывает входные сообщения
- Шлёт обработанные сообщения в *API*
- Отображает информацию для пользователя
### 1.2. API
Взаимодействие по Rest API  
Написан на Django REST framework
- Интерфейс обмена информацией между *Bot* и *DB*
### 1.3. DataBase
- Хранит информацию
## 2. Программная реализация
Основной файл - main.py
### 2.1. Bot
/bot/bot.py -  реализация бота
- Методы для создания / определения пользователя
  Каждому пользователю присваивается уникальный токен
- Методы для взаимодействия с пользователем
### 2.2. API

### 2.3. DataBase


# План модификации:

1. Возможность генерации или удаления пользователських категорий. Сделать это отдельным пунктом в меню. 

2. Выбор валюты

3. Скорректировать отчеты:

    - Добавить отчет за неделю

    - Переделать отчет за месяц

4. Хранить состояние пользователя в базе данных, а не в словаре 🤡

5. Выделить класс пользователя в отдельный файл

6. Создать класс Бота и переделать обработку сообщений. 

7. Поправить docker-compose 

8. Добавить напоминание пользователю о внесении расходов через Таски в Celery.

9. Таблицы
- сделать удобнее отрисовку
- добавить 3й столбец с % от total
- добавить возможность сортировки трат
