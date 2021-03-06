# ideal_schoolkid: Дневник отличника

Учебная задача в рамках модуля "Знакомство с Django: ORM — Урок 3. Взламываем электронный дневник" для учебной платформы [dvmn.org](https://dvmn.org)

Данный скрипт позволяет получить и изменить данные в школьном журнале на основе введенных данных пользователя.

А именно:
- исправление "плохих" ("двоек" и "троек") оценок на "отлично"
- удаление всех замечаний по конкретному ученику
- запись похвалы

# Подготовка к использованию

- Скачать из репозитория файл `magic.py`
- Скопировать файл `magic.py` в папку рядом с файлом `manage.py`
- запустить Django Shell командой 
```
python manage.py shell
```
- импортировать скрипт командой
```
from magic import start
```

# Использование

- Находясь в Django Shell, вызвать функцию start командой 
```
start()
```
- Следовать инструкциям на экране

# Пример работы

```console
Добро пожаловать в "Мир идеальных оценок!"
 Для продолжения необходимо найти ученика по его ФИО, а так же выбрать предмет

Введите ФИО школьника: поляков
Название предмета: труд
"Мир идеальных оценок!"
Ученик: Поляков Лонгин Адамович 1А
Предмет: Труд 1 класса
Меню:
1. Исправить все плохие оценки
2. Удалить все замечания
3. Записать похвалу
4. Изменить предмет
5. Выбрать другого ученика и предмет
6. Выход
Выберите пункт меню:

```
