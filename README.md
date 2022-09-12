Веб-сервер Flask доступен по адресу http://127.0.0.1:5000/perform_query/, который может выполнять запросы к файлу, хранящемуся в папке «данные».

Для выполнения запроса необходимо передать в запросе имя файла, имя команды и значение команды Необходимо передать ровно две команды за раз (не больше, не меньше)

Доступные команды

regex - фильтровать данные с переданным регулярным выражением
map - получить данные только из переданного столбца (обновление: строки разбиваются с помощью регулярных выражений)
filter - получить строки, содержащие переданную строку
уникальный - получить только уникальные данные
sort - сортировать данные в порядке возрастания или убывания
limit - ограничить строки до переданного числа
Запросить примеры

Команды могут быть переданы как параметры запроса **POST**

Пример: {
   "cmd1": "regex",
   "value1": "images/\\w+\\.png",
   "cmd2": "limit",
   "value2": "5"
}  