Данные для подключения к PostgreSQL базе данных:
логин: `user`
пароль: `password`
название БД: `dbname`
host: `0.0.0.0`
port: `5432`

Пример запроса:
`0.0.0.0:8000/ask-question?questions_num=75`

Пример запроса на загрузку аудиофайла:
```
curl -X 'POST' \
  'http://0.0.0.0:8000/user/add-audio?userId=4&token=ae1fd0e7-82e4-4760-b710-6c12f1b55dab' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@TestTask.wav;type=audio/wav'
```

Сборка/Запуск докер образа:
`make up`

Остановить докер образ:
`make down`

Вывести логи:
`make logs`
