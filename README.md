# Тестовое задание: Загрузка и обработка файлов
 
Данное приложение является Django REST API, которое позволяет загружать файлы на сервер, после чего аснхронно обрабатывает их через Celery.  

Отправка файл на сервер происходит через эндпоинт upload/, который принимает POST запрос и вовзвращает сериализованные данные файлы. Для проверка приложения используется Postman.  

Отправка файла на сервер через Postman:  
![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/0f4ef440-2d8e-4c8b-a14d-a3d864310e1d)  

Ответ:  
![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/ef78d817-9a28-45e5-937d-c9c77f08f1f6)  

После отправки файла на сервер запускается асинхронная задача Celery, изменяющая поле processed с False на True после обработки файла.
Каждая задача выполняется 5 секунд.  

Записи в БД:  
![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/c3ba0cca-ac99-44d4-810a-1910f747cb91)  

Работа Celery:  
![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/a15a6718-f5d7-4b82-ba9c-e5520e4af425)  

Второй эндпоинт files/, возвращающий список всех файлов с их данными и статусом обработки:  

GET-запрос:  
![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/f8e9c396-9652-4555-83ba-aa844518f930)  

Ответ:  
![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/f521e829-f709-44b8-ad78-bb9c67e0dbf7)  

Тестирование проводилось при помощи Locust.  
RPS на отправке файла около 6:  
![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/e0c59b9e-5eff-45e0-83d4-eddb25011c1c)  

RPS на получении списка файлов около 500:  
![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/0a7d08c3-413e-4968-9ec5-06316dcedecb)




Деплой приложения:  
http://urvatov.pythonanywhere.com/




