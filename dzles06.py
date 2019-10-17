# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

# from math import sqrt
# class Triangle:
#     def __init__(self, a, b, c):
#         l = sorted([a, b, c])
#         self.ab = int(sqrt((l[1][0] - l[0][0]) ** 2 + (l[1][1] - l[0][1]) ** 2))
#         self.bc = int(sqrt((l[2][0] - l[1][0]) ** 2 + (l[2][1] - l[1][1]) ** 2))
#         self.ac = int(sqrt((l[2][0] - l[0][0]) ** 2 + (l[2][1] - l[0][1]) ** 2))
#
#     def semiperimeter(self):
#         self.semiperimeter = (self.ab + self.bc + self.ac) / 2
#         return self.semiperimeter
#
#     def perimeter(self):
#         p = self.ab + self.bc + self.ac
#         return p
#
#     def area(self):
#         s = int(sqrt(self.semiperimeter * (self.semiperimeter - self.ab) * (self.semiperimeter - self.bc) * (self.semiperimeter - self.ac)))
#         return s
#
#     def height(self):
#         h = int(2 / self.ab * (sqrt(self.semiperimeter * (self.semiperimeter - self.ab) * (self.semiperimeter - self.bc) * (self.semiperimeter - self.ac))))
#         return h
#
# tr = Triangle((5, 7), (2, 3), (8, 4))
# print(tr.semiperimeter())
# print(tr.perimeter())
# print(tr.area())
# print(tr.height())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# from math import sqrt
# class Trapeze:
#     def __init__(self, a, b, c, d):
#         l = sorted([a, b, c, d])
#         self.ab = int(sqrt((l[1][0] - l[0][0]) ** 2 + (l[1][1] - l[0][1]) ** 2))
#         self.bc = int(sqrt((l[2][0] - l[1][0]) ** 2 + (l[2][1] - l[1][1]) ** 2))
#         self.cd = int(sqrt((l[3][0] - l[2][0]) ** 2 + (l[3][1] - l[2][1]) ** 2))
#         self.ad = int(sqrt((l[3][0] - l[0][0]) ** 2 + (l[3][1] - l[0][1]) ** 2))
#         #Диагонали трапеции:
#         self.ac = int(sqrt((l[2][0] - l[0][0]) ** 2 + (l[2][1] - l[0][1]) ** 2))
#         self.bd = int(sqrt((l[3][0] - l[1][0]) ** 2 + (l[3][1] - l[1][1]) ** 2))
#
#
#     def is_trap(self):
#         if self.ac == self.bd:
#             return True
#         else:
#             return False
#
#     def perimeter(self):
#         p = self.ab + self.bc + self.cd + self.ad
#         return p
#
#     def area(self):
#         s = int(((self.ad + self.bc) / 4) * (sqrt(4 * (self.ab ** 2) - ((self.ad - self.bc) ** 2))))
#         return s
#
#
# trap = Trapeze((0, 0), (11, 5), (14, 0), (3, 5))
# print(trap.is_trap())
# print(trap.perimeter())
# print(trap.area())


# Задание-1:
# Реализуйте описанную ниже задачу, используя парадигмы ООП:
# В школе есть Классы (5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя (мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# Но больше математику не может преподавать никто другой.
# Выбранные и заполненные данные структуры должны решать следующие задачи :
# 1. Получить полный список всех классов школ++++++++++++++++++++++
# 2. Получить список всех учеников в указанном классе ++++++++++++++
#   (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#   (Ученик -> Класс -> Учителя -> Предметы)
# 4. Узнайте ФИО родителей указанного ученика++++++++++++++++++
# 5. Получить список всех Учителей, преподающих в указанном классе+++++++++++++++
class People:
    def __init__(self, surname, name, middle, classroom):
        self.name = name
        self.surname = surname
        self.middle = middle
        self.classroom = classroom

    def get_full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.middle

    def initials(self):
        return ('{} {:.1}.{:.1}.'.format(self.surname, self.name,self.middle))

class Student(People):
    def __init__(self, surname, name, middle, classroom, parents):
        People.__init__(self, surname, name, middle, classroom)
        self.parents = parents

    def am_I_in_class(self, value):
        if self.classroom == value:
            return True
        else:
            return False

    def stud_in_class(self, value):
        if self.surname == value:
            return True
        else:
            return False



class Teacher(People):
    def __init__(self, surname, name, middle, classroom, subject):
        People.__init__(self, surname, name, middle, classroom)
        self.subject = subject

    def am_I_in_class(self, value):
        if self.classroom == value:
            return True
        else:
            return False

    def initials(self):
        return ('{} {:.1}.{:.1}.'.format(self.surname, self.name,self.middle))

# class School:
#     def __init__(self, classroom, subject):
#         self.subject = subject
#         self.classroom = classroom
#
#     def sub_in_class(self, value):
#         if self.subject == value:
#             return True
#         else:
#             return False
#
#
# school = School
teachers = [Teacher("Иванов", "Иван", "Иванович", "3а", "Математика"),
            Teacher("Петров", "Петр", "Петрович", "3а", "Русский язык"),
            Teacher("Смирнов", "Семен", "Семонович", "7б", "Литература"),
            Teacher("Сидоров", "Сидр", "Сидрович", "7б", "История"),
            Teacher("Попов", "Виктор", "Викторович", "5в", "Физика"),
            Teacher("Васильев", "Василий", "Васильевич", "5в", "Химия"),
            ]

students = [Student("Иванов", "Алексей", "Олегович", "3а", "Иванова Ольга Петровна и Иванов Олег Васильевич"),
            Student("Петров", "Александр", "Евгеньевич", "3а", "Петрова Людмила Михайловна и Петров Евгений Владимирович"),
            Student("Смирнов", "Николай", "Михайлович", "7б", "Смирнова Ирина Андреевна и Смирнов Михаил Юрьевич"),
            Student("Сидоров", "Артем", "Николаевич", "7б", "Сидорова Юлия Константиновна и Сидоров Николай Николаевич"),
            Student("Попов", "Олег", "Константинович", "5в", "Попова Мария Васильевна и Попов Константин Петрович"),
            Student("Кудрявцев", "Василий", "Анатольевич", "5в", "Кудрявцева Надежда Николаевна и Кудрявцев анатолий Юрьевич"),
            ]


# number_class = input('Введите интересующий Вас класс\n')
# print([student.initials() for student in students if student.am_I_in_class(number_class)])
# print([student.initials() for student in students if student.am_I_in_class(number_class)])

# print(set([x.classroom for x in students]))
#
# print([x.initials() for x in teachers if x.classroom == number_class])

#print([x.parents for x in students if x.name == 'Иванов'])

# choose_student = input('Введите фамилию интересующего Вас ученика\n')
# print([student.classroom for student in students if student.stud_in_class(choose_student)])
