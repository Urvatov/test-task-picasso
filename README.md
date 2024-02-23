# Тестовое задание: Загрузка и обработка файлов
 
Данное приложение является Django REST API, которое позволяет загружать файлы на сервер, после чего аснхронно обрабатывает их через Celery.  

Отправка файл на сервер происходит через эндпоинт upload/, который принимаеи POST запрос и вовзвращает сериализованные данные файлы. Для проверка приложения используется Postman.  

Отправка файла на сервер через Postman:  
![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/0f4ef440-2d8e-4c8b-a14d-a3d864310e1d)  

Ответ:
![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/ef78d817-9a28-45e5-937d-c9c77f08f1f6)  

После отправки файла на сервер запускается асинхронная задача Celery, изменяющая поле processed с False на True после обработки файла.  Каждая задача выполняется 5 секунд.


![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/c3ba0cca-ac99-44d4-810a-1910f747cb91)
![изображение](https://github.com/Urvatov/test-task-picasso/assets/117490456/a15a6718-f5d7-4b82-ba9c-e5520e4af425)
