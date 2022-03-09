class Describe(object):
    def __init__(self):
        self.fool_dict = {}
        self.dict_courses = {}

    def choose_course(self, users, courses):
        students = dict()
        for j in courses:
            for k in users:
                students[k.show()] = 0
            self.fool_dict[j.show()] = students.copy()
        return self.fool_dict

    def exam(self, dict_courses):
        self.dict_courses = dict_courses
        for i in dict_courses:
            for j in (dict_courses[i]):
                print('Предмет:', i)
                print('Ваше имя:', j)
                print('Всего 10 вопросов', 'На сколько ответов вы правильно ответили?', sep='\n')
                answers = int(input())
                if 0 <= answers < 5:
                    self.dict_courses[i][j] = 2
                if 5 <= answers < 7:
                    self.dict_courses[i][j] = 3
                if 7 <= answers < 9:
                    self.dict_courses[i][j] = 4
                if 9 <= answers <= 10:
                    self.dict_courses[i][j] = 5
        return self.dict_courses


class Show(object):
    def user(self, users):
        print('Пользователи системы:')
        for i in users:
            print(i.show())
        print()

    def course(self, courses):
        print('Существующие курсы:')
        for j in courses:
            print(j.show())
        print()

    def results(self):
        print('Результаты по курсам:')
        print(Courses.choose_course)
        print()


class Customer(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show(self):
        return self.name


class Courses(object):
    def __init__(self, subject):
        self.subject = subject
        self.choices = None
        self.exam_marks = None

    def choose_course(self):
        return self.choices

    def exam(self):
        return self.exam_marks

    def show(self):
        return self.subject


user1 = Customer(1, 'Bogdan')
user2 = Customer(2, 'Tonya')
user3 = Customer(3, 'Tanya')
course1 = Courses('Математика')
course2 = Courses('Физика')
course3 = Courses('Химия')

customers = [user1, user2, user3]
subjects = [course1, course2, course3]

educ_system = Describe()

dict_subjects = educ_system.choose_course(customers, subjects)  # Зачисление на курс
Courses.choose_course = dict_subjects

exam_results = educ_system.exam(dict_subjects)  # Результаты экзамена
Courses.exam_marks = exam_results

Show().user(customers)  # Пользователи
Show().course(subjects)  # Курсы
Show().results()  # Результаты по курсам
