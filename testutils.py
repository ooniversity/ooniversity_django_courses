import datetime

from students.models import Student
from courses.models import Course, Lesson


# --- Funtions creation objects (courses, students and lessons) ---

def create_course(title, sh_descr, descript, coach=None, assistant=None):
    # Create course without coaches
    course = Course.objects.create(title=title, short_descript=sh_descr,
                                                      description=descript)
    # Add coache and assistant in course, if they defined
    if coach != None:
        course.coach.add(coach)
    if assistant != None:
        course.assistant.add(assistant)
    return course

def create_student(name, surname, date, email, skype, phone, addr, courses=None):
    # Create student without courses
    student = Student.objects.create(
        name=name, surname=surname,
        date_of_birth=datetime.datetime.strptime(date, '%d-%m-%Y').date(),
        email=email, skype=skype, phone=phone, address=addr
    )
    # Add courses in student, if they defined
    if courses != None:
        for stud_course in courses:
            student.courses.add(stud_course)
    return student

def create_lesson(number, theme, descript, course):
    # Create lesson with course
    lesson = Lesson.objects.create(
        number=number, theme=theme, description=descript,
        course=course
    )
    return lesson

