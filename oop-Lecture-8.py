class Student:
    def __init__(self, name, surname, gender):
        self.courses_attached = []
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        def add_courses(self, course_name):
            self.finished_course.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        count = 0
        summa = 0
        for grade_list in self.grades.values():
            for grade in grade_list:
                count += 1
                summa += grade
        if count==0:
            count=1
        average = summa / count
        return average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_rating() < other.average_rating()


    def __str__(self):
        result = ''
        result += 'Имя: ' + self.name + '\n'
        result += 'Фамилия: ' + self.surname + '\n'
        result += 'Средняя оценка за ДЗ: ' + str(self.average_rating())+'\n'
        result += 'Курсы в процессе изучения: '+ ", ".join(self.courses_in_progress)+'\n'
        result += 'Завершённые курсы: ' + ", ".join(self.finished_courses)
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average = 0
        self.courses_in_progress = []
        self.grades = {}

    def average_rating(self):
        count = 0
        summa = 0
        for grade_list in self.grades.values():
            for grade in grade_list:
                count += 1
                summa += grade
        if count==0:
            count=1
        average = summa / count
        return average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rating() < other.average_rating()


    def __str__(self):
        result = ''
        result += 'Имя: ' + self.name + '\n'
        result += 'Фамилия: ' + self.surname + '\n'
        result += 'Средняя оценка за лекции: ' + str(self.average_rating())
        return result


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = ''
        result += 'Имя: ' + self.name + '\n'
        result += 'Фамилия: ' + self.surname
        return result


kevin_adamson = Student('Kevin', 'Adamson', 'your_gender')
kevin_adamson.courses_in_progress += ['Python','Git']
kevin_adamson.finished_courses += ['Введение в программирование']
kevin_adamson.courses_attached += ['Python']

andrew_aldridge = Student('Andrew', 'Aldridge', 'your_gender')
andrew_aldridge.courses_in_progress += ['Python','Git']
andrew_aldridge.finished_courses += ['Введение в программирование']
andrew_aldridge.courses_attached += ['Python']

ben_evans = Reviewer('Ben', 'Evans')
ben_evans.courses_attached += ['Python']
ben_evans.rate_hw(kevin_adamson, 'Python', 7)
ben_evans.rate_hw(kevin_adamson, 'Python', 8)
ben_evans.rate_hw(kevin_adamson, 'Python', 5)

alexander_johnson = Reviewer('Alexander', 'Johnson')
alexander_johnson.courses_attached += ['Python']
alexander_johnson.rate_hw(andrew_aldridge, 'Python', 7)
alexander_johnson.rate_hw(andrew_aldridge, 'Python', 10)
alexander_johnson.rate_hw(andrew_aldridge, 'Python', 5)

andrew_davies = Lecturer('Andrew', 'Davies')
andrew_davies.courses_in_progress += ['Python']
kevin_adamson.rate_hw(andrew_davies, 'Python', 10)
kevin_adamson.rate_hw(andrew_davies, 'Python', 9)
kevin_adamson.rate_hw(andrew_davies, 'Python', 9)

samuel_wilson = Lecturer('Samuel', 'Wilson')
samuel_wilson.courses_in_progress += ['Python']
andrew_aldridge.rate_hw(samuel_wilson, 'Python', 10)
andrew_aldridge.rate_hw(samuel_wilson, 'Python', 9)
andrew_aldridge.rate_hw(samuel_wilson, 'Python', 8)

print(kevin_adamson)
print()
print(andrew_aldridge)
print()
print(ben_evans)
print()
print(alexander_johnson)
print()
print(andrew_davies)
print()
print(samuel_wilson)
print()
print (f'Оценка, {kevin_adamson.name} ,меньше чем у {andrew_aldridge.name} - {kevin_adamson. __lt__ (andrew_aldridge)}')
print()
print (f'Оценка, {andrew_davies.name} {andrew_davies.surname} ,меньше чем у {samuel_wilson.name} {samuel_wilson.surname} - {andrew_davies. __lt__ (samuel_wilson)}')

list_student = [kevin_adamson, andrew_aldridge]
course = 'Python'
list_lecturer = [andrew_davies, samuel_wilson]


def students_average_rating (list_student):
    vocabulary_of_grades = {}
    list_of_grades = []
    sum_of_ratings = 0
    count = 0
    for student in list_student:
        if course in student.grades:
            vocabulary_of_grades = student.grades
            for list_of_grades in vocabulary_of_grades.values():
                for grade in list_of_grades:
                    count +=1
                    sum_of_ratings+=grade
        else:
          print('Такого курса нет в программе')
          count = 1
          break
    average_ratings = sum_of_ratings/count
    print (f'Средняя оценка за курс {course} для всех студентов равна: {average_ratings}')

students_average_rating (list_student)


def lecturer_average_rating (list_lecturer):
    vocabulary_of_grades = {}
    list_of_grades = []
    sum_of_ratings = 0
    count = 0
    for lecturer in list_lecturer:
        if course in lecturer.grades:
            vocabulary_of_grades = lecturer.grades
            for list_of_grades in vocabulary_of_grades.values():
                for grade in list_of_grades:
                    count +=1
                    sum_of_ratings+=grade
        else:
          print('Такого курса нет в программе')
          count = 1
          break
    average_ratings = sum_of_ratings/count
    print (f'Средняя оценка за курс {course} для всех лекторов равна: {average_ratings}')

lecturer_average_rating (list_lecturer)
