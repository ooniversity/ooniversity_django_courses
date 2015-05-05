# -*- coding: utf-8 -*-


# --- БЛОК ДАННЫХ ---

# -- DATA for create Courses --

def get_course_1():
    # Course DATA / COURSE_1
    TITLE = 'PY101'
    SH_DESCR = u'Введение в Python'
    DESCRIPT = u'Знакомство с основами Python!'
    # Формирование кортежа данных
    COURSE_1 = (TITLE, SH_DESCR, DESCRIPT)
    return COURSE_1

def get_course_2():
    # Course DATA / COURSE_2
    TITLE = 'DJ101'
    SH_DESCR = u'Фреймворк Django'
    DESCRIPT = u'Web разработка на Python/Django!'
    # Формирование кортежа данных
    COURSE_2 = (TITLE, SH_DESCR, DESCRIPT)
    return COURSE_2

def get_course_3():
    # Course DATA / COURSE_3
    TITLE = 'JS'
    SH_DESCR = u'JavaScript'
    DESCRIPT = u'Обучение программированию на JavaScript!'
    # Формирование кортежа данных
    COURSE_3 = (TITLE, SH_DESCR, DESCRIPT)
    return COURSE_3

def get_course_4():
    # Course DATA / COURSE_4
    TITLE = 'RUBI'
    SH_DESCR = u'Ruby on Rails'
    DESCRIPT = u'Веб-программирование на Ruby on Rails!'
    # Формирование кортежа данных
    COURSE_4 = (TITLE, SH_DESCR, DESCRIPT)
    return COURSE_4


# -- DATA for create Students --

def get_student_1():
    # Student DATA / STUDENT_1
    NAME = u'Алёша'
    SURNAME = u'Попов'
    DATE = '15-09-1985'
    EMAIL = 'popovi4@some.com'
    SKYPE = 'alyo-popov'
    PHONE = '+380976676613'
    ADDR = u'г.Киев, ул. Сомова 15, кв.98'
    # Формирование кортежа данных
    STUDENT_1 = (NAME, SURNAME, DATE, EMAIL, SKYPE, PHONE, ADDR)
    return STUDENT_1

def get_student_2():
    # Student DATA / STUDENT_2
    NAME = u'Сергей'
    SURNAME = u'Власов'
    DATE = '21-03-1988'
    EMAIL = 'vlasov4@ukr.net'
    SKYPE = 'ser-vlass'
    PHONE = '+380956632211'
    ADDR = u'г.Херсон, ул. Камила 32, кв.13'
    # Формирование кортежа данных
    STUDENT_2 = (NAME, SURNAME, DATE, EMAIL, SKYPE, PHONE, ADDR)
    return STUDENT_2

def get_student_3():
    # Student DATA / STUDENT_3
    NAME = u'Влад'
    SURNAME = u'Корин'
    DATE = '08-11-1989'
    EMAIL = 'vladik1989@mail.ru'
    SKYPE = 'korinv-89'
    PHONE = '+380501136619'
    ADDR = u'г.Киев, ул. Караваева 46, кв.27'
    # Формирование кортежа данных
    STUDENT_3 = (NAME, SURNAME, DATE, EMAIL, SKYPE, PHONE, ADDR)
    return STUDENT_3

def get_student_4():
    # Student DATA / STUDENT_4
    NAME = u'Пётр'
    SURNAME = u'Фокин'
    DATE = '12-06-1990'
    EMAIL = 'fokin-90@gmail.com'
    SKYPE = 'fokin-pet'
    PHONE = '+380936586622'
    ADDR = u'г.Львов, ул. Домова 31, кв.9'
    # Формирование кортежа данных
    STUDENT_4 = (NAME, SURNAME, DATE, EMAIL, SKYPE, PHONE, ADDR)
    return STUDENT_4


# -- DATA for create Lessons --

def get_lesson_1():
    # Lesson DATA / LESSON_1
    NUM = 1
    THEME = u'Основы Python'
    DESCRIPT = u'ZEN, PEP8, типы данных, операторы (if, for...), исключения и разбор стектрейса.'
    # Формирование кортежа данных
    LESSON_1 = (NUM, THEME, DESCRIPT)
    return LESSON_1

def get_lesson_2():
    # Lesson DATA / LESSON_2
    NUM = 2
    THEME = u'Строки и итераторы'
    DESCRIPT = u'Работа со строками и итерируемыми типами данных, запуск скрипта и параметры.'
    # Формирование кортежа данных
    LESSON_2 = (NUM, THEME, DESCRIPT)
    return LESSON_2

def get_lesson_3():
    # Lesson DATA / LESSON_3
    NUM = 3
    THEME = u'Функции и модульность'
    DESCRIPT = u'Функции (def, lambda), модули и структура прорраммы.'
    # Формирование кортежа данных
    LESSON_3 = (NUM, THEME, DESCRIPT)
    return LESSON_3

