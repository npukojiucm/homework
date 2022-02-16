from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_grades(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка!'

    def __mean(self):
        if len(self.grades.values()) == 0:
            return 0
        grade = []
        for cour_grade in self.grades.values():
            for grade_ in cour_grade:
                grade.append(grade_)
        return round(mean(grade), 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other.name} {other.surname} не является студентом')
            return
        return self.__mean() < other.__mean()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print(f'{other.name} {other.surname} не является студентом')
            return
        return self.__mean() > other.__mean()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print(f'{other.name} {other.surname} не является студентом')
            return
        return self.__mean() == other.__mean()

    def __str__(self):
        info = f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.__mean()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return info


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student_, course, grade):
        if isinstance(student_, Student) and course in student_.courses_in_progress:
            if course in student_.grades:
                student_.grades[course] += [grade]
            else:
                student_.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        info = f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'
        return info


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __mean(self):
        if len(self.grades.values()) == 0:
            return 0
        grade = []
        for cour_grade in self.grades.values():
            for grade_ in cour_grade:
                grade.append(grade_)
        return round(mean(grade), 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other.name} {other.surname} не является лектором')
            return
        return self.__mean() < other.__mean()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other.name} {other.surname} не является лектором')
            return
        return self.__mean() > other.__mean()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other.name} {other.surname} не является лектором')
            return
        return self.__mean() == other.__mean()

    def __str__(self):
        info = f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.__mean()}'
        return info


def mean_grade_course(list_, course):
    grade = []
    for student_ in list_:
        for key_, value_ in student_.grades.items():
            if key_ == course:
                for grades in value_:
                    grade.append(grades)
    info = f'Средняя оценка потока за домашние задания по курсу {course} - {round(mean(grade), 1)}'
    info_ = f'Средняя оценка лекторов за лекции по курсу {course} - {round(mean(grade), 1)}'
    if isinstance(list_[0], Student):
        return info
    elif isinstance(list_[0], Lecturer):
        return info_
    else:
        return 'Ошибка'


student1 = Student('Ivan', 'Ivanov', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.add_courses('C++')
student1.add_courses('Java')

student2 = Student('Liza', 'Petrova', 'female')
student2.courses_in_progress += ['Python', 'C#']
student2.add_courses('C++')
student2.add_courses('Java')

student3 = Student('Nina', 'Kozlova', 'female')
student3.courses_in_progress += ['Git', 'C#']
student3.add_courses('C++')
student3.add_courses('Java')

reviewer1 = Reviewer('Masha', 'Kozlova')
reviewer2 = Reviewer('Dasha', 'Pavlova')
reviewer3 = Reviewer('Andrey', 'Akopayn')

lecturer1 = Lecturer('Oleg', 'Vitko')
lecturer2 = Lecturer('Karina', 'Kop')
lecturer3 = Lecturer('Kolay', 'Mishenko')

lecturer1.courses_attached += ['Git', 'C#']
lecturer2.courses_attached += ['Git', 'Python']
lecturer3.courses_attached += ['Python', 'C#']

reviewer1.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student1, 'Python', 2)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student1, 'Git', 1)
reviewer2.rate_hw(student1, 'Git', 7)
reviewer2.rate_hw(student1, 'Git', 4)

reviewer1.rate_hw(student2, 'Python', 3)
reviewer1.rate_hw(student2, 'Python', 5)
reviewer1.rate_hw(student2, 'Python', 7)
reviewer3.rate_hw(student2, 'C#', 2)
reviewer3.rate_hw(student2, 'C#', 4)
reviewer3.rate_hw(student2, 'C#', 9)

reviewer2.rate_hw(student3, 'Git', 8)
reviewer2.rate_hw(student3, 'Git', 4)
reviewer2.rate_hw(student3, 'Git', 9)
reviewer3.rate_hw(student3, 'C#', 2)
reviewer3.rate_hw(student3, 'C#', 1)
reviewer3.rate_hw(student3, 'C#', 4)

student1.add_grades(lecturer1, 'Git', 6)
student1.add_grades(lecturer1, 'Git', 8)
student1.add_grades(lecturer1, 'Git', 4)
student1.add_grades(lecturer2, 'Git', 3)
student1.add_grades(lecturer2, 'Git', 9)
student1.add_grades(lecturer2, 'Git', 7)
student1.add_grades(lecturer2, 'Python', 2)
student1.add_grades(lecturer2, 'Python', 5)
student1.add_grades(lecturer2, 'Python', 6)
student1.add_grades(lecturer3, 'Python', 7)
student1.add_grades(lecturer3, 'Python', 6)
student1.add_grades(lecturer3, 'Python', 4)

student2.add_grades(lecturer1, 'C#', 1)
student2.add_grades(lecturer1, 'C#', 5)
student2.add_grades(lecturer1, 'C#', 7)
student2.add_grades(lecturer2, 'Python', 9)
student2.add_grades(lecturer2, 'Python', 5)
student2.add_grades(lecturer2, 'Python', 2)
student2.add_grades(lecturer3, 'Python', 4)
student2.add_grades(lecturer3, 'Python', 8)
student2.add_grades(lecturer3, 'Python', 7)
student2.add_grades(lecturer3, 'C#', 7)
student2.add_grades(lecturer3, 'C#', 6)
student2.add_grades(lecturer3, 'C#', 9)

student3.add_grades(lecturer1, 'Git', 5)
student3.add_grades(lecturer1, 'Git', 6)
student3.add_grades(lecturer1, 'Git', 8)
student3.add_grades(lecturer1, 'C#', 8)
student3.add_grades(lecturer1, 'C#', 4)
student3.add_grades(lecturer1, 'C#', 9)
student3.add_grades(lecturer2, 'Git', 9)
student3.add_grades(lecturer2, 'Git', 2)
student3.add_grades(lecturer2, 'Git', 5)
student3.add_grades(lecturer3, 'C#', 7)
student3.add_grades(lecturer3, 'C#', 5)
student3.add_grades(lecturer3, 'C#', 6)

student = [student1, student2, student3]
lecturer = [lecturer1, lecturer2, lecturer3]

print(student1)
print()
print(student2)
print()
print(student3)
print()
print(reviewer1)
print()
print(reviewer2)
print()
print(reviewer3)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(lecturer3)
print()
print(student1 == student2)
print(student1 < student2)
print(student1 == reviewer3)
print(student1 < lecturer1)
print()
print(lecturer1 > lecturer2)
print(lecturer1 == lecturer2)
print(lecturer1 == reviewer1)
print(lecturer1 < student1)
print()
print(mean_grade_course(student, 'Python'))
print(mean_grade_course(student, 'Git'))
print(mean_grade_course(student, 'C#'))
print()
print(mean_grade_course(lecturer, 'Python'))
print(mean_grade_course(lecturer, 'Git'))
print(mean_grade_course(lecturer, 'C#'))
