from datetime import date
from views import Index, About, Contact, StudyPrograms, CoursesList, CreateCourse,\
    CreateCategory, CategoryList, CopyCourse


def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/about/': About(),
    '/contact/': Contact(),
    '/study_programs/': StudyPrograms(),
    '/courses_list/': CoursesList(),
    '/create_course/': CreateCourse(),
    '/create_category/': CreateCategory(),
    '/category_list/': CategoryList(),
    '/copy_course/': CopyCourse()
}
