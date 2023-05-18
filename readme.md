При наличии Makefile установленного на системе
проект собирается/запускается следующим образом:

* Сборка/Запуск докер образа: `make up`
* Остановить докер образ: `make down`
* Вывести логи: `make logs`
* Сделать миграции в alembic: `make migrate-alembic`

При отсутствии Makefile:

* Сборка/Запуск докер образа: `docker compose up -d`
* Остановить докер образ: `docker compose down`
* Вывести логи: `docker compose logs app -f`
* Сделать миграции в alembic: 
  * `docker compose exec app alembic revision --autogenerate`
  `docker compose exec app alembic upgrade head`

-------------------

Данные для подключения к PostgreSQL базе данных:

* логин: `user`
* пароль: `password`
* название БД: `dbname`
* host: `0.0.0.0`
* port: `5432`

-------------------

Автогенерируемая документация доступна на `http://0.0.0.0:8000/docs`

Пример запроса викторины:
```
curl --location --request POST '0.0.0.0:8000/ask-question?questions_num=15'
```

Пример запроса на создание пользователя
```
curl --location --request POST '0.0.0.0:8000/user/create?username=AkimDuyshenaliev'
```

Пример запроса на загрузку аудиофайла:
```
curl -X 'POST' \
  'http://0.0.0.0:8000/user/add-audio?userId=1&token=11ed9adb-5e1a-41af-9c74-90171fc436d5' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@TestTask.wav;type=audio/wav'
```

Пример запроса на скачивание аудиофайла:
```
curl --location '0.0.0.0:8000/record?id=5&user=1'
```