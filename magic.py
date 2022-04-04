import os
import random

import datacenter
from datacenter.models import (Chastisement, Commendation, Subject,
                               Lesson, Mark, Schoolkid)
COMMENDATIONS = [
'Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!',
'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!',
'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!',
'Очень хороший ответ!', 'Талантливо!',
'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!',
'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!',
'Ты на верном пути!', 'Здорово!', 'Это как раз то, что нужно!',
'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!',
'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!',
'Ты растешь над собой!', 'Ты многое сделал, я это вижу!',
'Теперь у тебя точно все получится!'
]


def create_commendation(schoolkid, subject):
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject=subject
    ).order_by('date').last()

    Commendation.objects.create(
        text=random.choice(COMMENDATIONS),
        created=lesson.date,
        schoolkid=schoolkid,
        subject=subject,
        teacher=lesson.teacher
    )
    return f'Добавлена похвала.' \
           f'Ученик: {schoolkid},' \
           f' Урок: {lesson.subject}, дата: {lesson.date}'


def remove_chastisements(schoolkid):
    all_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    all_chastisements.delete()


def fix_marks(schoolkid):
    marks = Mark.objects.filter(points__lte=3, schoolkid=schoolkid)
    for mark in marks:
        mark.points = 5
        mark.save()


def get_schoolkid():
    while True:
        schoolkid_name = input('Введите ФИО школьника: ').title()
        try:
            schoolkid = Schoolkid.objects.get(
                full_name__contains=schoolkid_name
            )
        except datacenter.models.Schoolkid.MultipleObjectsReturned as err:
            print('Найдено несколько учеников с этим именем. '
                  'Уточните ФИО ученика\n', err)
        except datacenter.models.Schoolkid.DoesNotExist as err:
            print(f'Ученик с именем {schoolkid_name} не найден.')
        else:
            break
    return schoolkid


def get_subject(schoolkid):
    while True:
        subject_name = input('Название предмета: ').title()
        try:
            subject = Subject.objects.get(
                title__contains=subject_name,
                year_of_study=schoolkid.year_of_study)
        except (datacenter.models.Subject.MultipleObjectsReturned,
                datacenter.models.Subject.DoesNotExist):
            print('Такого предмета у ученика нет')
        else:
            break
    return subject


def start():
    title = '"Мир идеальных оценок!"'
    print(
        f'Добро пожаловать в {title}\n',
        'Для продолжения необходимо найти ученика по его ФИО, '
        'а так же выбрать предмет\n')
    while True:
        schoolkid = get_schoolkid()
        subject = get_subject(schoolkid)
        while True:
            message = ''
            print(title)
            print('Ученик:', schoolkid, '\nПредмет:', subject)
            print('Меню:\n'
                  '1. Исправить все плохие оценки\n'
                  '2. Удалить все замечания\n'
                  '3. Записать похвалу\n'
                  '4. Изменить предмет\n'
                  '5. Выбрать другого ученика и предмет\n'
                  '6. Выход')
            item_num = int(input('Выберите пункт меню: '))
            if item_num == 1:
                fix_marks(schoolkid)
                message = 'Все плохие оценки исправлены'
            elif item_num == 2:
                remove_chastisements(schoolkid)
                message = 'Все замечания удалены'
            elif item_num == 3:
                message = create_commendation(schoolkid, subject)
            elif item_num == 4:
                subject = get_subject(schoolkid)
                message = ''
            elif item_num == 5:
                break
            elif item_num == 6:
                return
            os.system("cls" if os.name == "nt" else "clear")
            print(message)
            input('Для продолжения нажмите Enter')
        os.system("cls" if os.name == "nt" else "clear")
