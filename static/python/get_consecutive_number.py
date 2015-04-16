from courses.models import Lesson


def get_consecutive_number(pk):
    consecutive_number_list=[]
    for i in Lesson.objects.filter(course_id=pk):
        consecutive_number_list.append(i.consecutive_number)
    consecutive_number_list.sort()
    if len(consecutive_number_list):
        if consecutive_number_list[0] != 1:
            number = 1
        elif consecutive_number_list==[i for i in xrange(1,consecutive_number_list[-1]+1)]:
            number = consecutive_number_list[-1] + 1
        else:
            set_number, set_range=set(), set()
            set_number.update(consecutive_number_list)
            set_range.update(xrange(1,consecutive_number_list[-1]+1))
            set_range.difference_update(set_number)
            consecutive_number_list=[]
            consecutive_number_list.extend(set_range)
            consecutive_number_list.sort()
            number=consecutive_number_list[0]
    else:
        number = 1
    return number