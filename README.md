# YamDB
REST API для сервиса YamDB

# Модели
Отзывы:

+ получить список всех отзывов;
+ создать новый отзыв;
+ получить отзыв по id;
+ частично обновить отзыв по id;
+ удалить отзыв по id.

Комментарии к отзывам:

+ Получить список всех комментариев к отзыву по id;
+ создать новый комментарий для отзыва, получить комментарий для отзыва по id;
+ частично обновить комментарий к отзыву по id;
+ удалить комментарий к отзыву по id.

JWT-токен:

+ Отправление confirmation_code на переданный email;
+ получение JWT-токена в обмен на email и confirmation_code.

Пользователи:

+ получить список всех пользователей;
+ создание пользователя получить пользователя по username;
+ изменить данные пользователя по username;
+ удалить пользователя по username;
+ получить данные своей учетной записи;
+ изменить данные своей учетной записи.

Категории (типы) произведений:

+ получить список всех категорий;
+ создать категорию;
+ удалить категорию.

Категории жанров:

+ получить список всех жанров
+ создать жанр;
+ удалить жанр.

Произведения, к которым пишут отзывы:

+ получить список всех объектов;
+ создать произведение для отзывов;
+ информация об объекте;
+ обновить информацию об объекте;
+ удалить произведение.

# Алгоритм регистрации пользователей

1. Пользователь отправляет запрос с параметром email на /auth/email/.
2. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
3. Пользователь отправляет запрос с параметрами email и confirmation_code на /auth/token/, в ответе на запрос ему приходит token (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на /users/me/ и заполняет поля в своём профайле (описание полей — в документации).

# Пользовательские роли

- Аноним — может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить рейтинг произведениям (фильмам/книгам/песням), может комментировать чужие отзывы и ставить им оценки; может редактировать и удалять свои отзывы и комментарии.
- Модератор — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
- Администратор — полные права на управление проектом и всем его содержимым. Может создавать и удалять категории и произведения. Может назначать роли пользователям.
- Администратор Django — те же права, что и у роли Администратор.

# Запуск сервиса

1. git clone ***git@github.com:bitcoineazy/infra_sp2.git***
2. Создать файл .env со значениями: ***DB_ENGINE=django.db.backends.postgresql, DB_NAME=postgres, POSTGRES_USER=postgres, POSTGRES_PASSWORD=postgres, DB_HOST=db, DB_PORT=5432***
3. Запустить Docker: ***sudo docker-compose up***
4. Выполнить миграции внутри докера: ***sudo docker-compose exec web python manage.py makemigrations && sudo docker-compose exec web python manage.py migrate***
5. Создать профиль администратора внутри докера: ***sudo docker-compose exec web python manage.py createsuperuser***
6. Собрать всю статику внутри докера: ***sudo docker-compose exec web python manage.py collectstatic***
7. Загрузка тестовых данных ***sudo docker-compose exec web python manage.py loaddata fixtures.json***
