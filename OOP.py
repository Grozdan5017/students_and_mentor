class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_ls(self, lecrurer, course, grade):
        if isinstance(lecrurer, Lecturer) and course in lecrurer.courses_attached and grade <= 10 \
                and course in self.courses_in_progress:
            if course in lecrurer.grades:
                lecrurer.grades[course] += [grade]
            else:
                lecrurer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        sum_rating = 0
        len_rating = 0
        for rating in self.grades.values():
            sum_rating += sum(rating)
            len_rating += len(rating)
        rating_average = round(sum_rating / len_rating, 2)
        return rating_average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: ' \
              f'{self.average_rating()}\nКурсы в процессе обучения: {",".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res

    def __lt__(self, his):
        if not isinstance(his, Student):
            print("Студентов и преподователей между собой не сравнивают!")
            return
        return self.average_rating() < his.average_rating()

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):  # Эксперты
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


class Lecturer(Mentor):  # Лекторы
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_score(self):
        sum_score = 0
        len_score = 0
        for score in self.grades.values():
            sum_score += sum(score)
            len_score += len(score)
        score_average = round(sum_score / len_score, 2)
        return score_average

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.average_score()}"
        return res

    def __lt__(self, his):
        if not isinstance(his, Lecturer):
            print("Студентов и преподавателей между собой не сравнивают!")
            return
        return self.average_score() < his.average_score()

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating


# Студенты
student_1 = Student('Денис', 'Казанцев', 'Муж.')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Основы языка программирования Python', 'Git- система контроля версий']

student_2 = Student('Дмитрий', 'Колосов', 'Муж.')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Основы Java']

# Эксперты
reviewer_1 = Reviewer('Василий', 'Петров')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Николай', 'Маратканов')
reviewer_2.courses_attached += ['Java', 'Git']

# Лекторы
lecturer_1: Lecturer = Lecturer('Владимир', 'Зуев')
lecturer_1.courses_attached += ['Java', 'Git']

lecturer_2 = Lecturer('Владислав', 'Федотов')
lecturer_2.courses_attached += ['Python']

# Оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Java', 10)
reviewer_2.rate_hw(student_2, 'Java', 5)
reviewer_2.rate_hw(student_2, 'Java', 3)

reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_1, 'Git', 5)
reviewer_2.rate_hw(student_1, 'Git', 7)

# Оценки лекторам
student_1.rate_ls(lecturer_1, 'Git', 8)
student_1.rate_ls(lecturer_2, 'Python', 5)
student_1.rate_ls(lecturer_1, 'Git', 8)
student_1.rate_ls(lecturer_2, 'Python', 10)

student_2.rate_ls(lecturer_1, 'Java', 2)
student_2.rate_ls(lecturer_1, 'Java', 10)
student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def average_rating_for_course(self):  # Средняя оценка
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


print('Сравнение по средним оценкам:')
print('student_1 < student_2 ', student_1 < student_2)
# noinspection PyTypeChecker
print('student_1 < lecturer_1 ', student_1 < lecturer_1)
print('lecturer_1 > lecturer_2 ', lecturer_1 > lecturer_2)
print()
print(f"Студенты:\n {student_1}\n\n {student_2}")
print()
print()
print(f"Эксперты:\n {reviewer_1}\n\n {reviewer_2}")
print()
print(f"Лекторы:\n {lecturer_1}\n\n {lecturer_2}")
print()
print(f"Средняя оценка за домашнее задание: {average_rating_for_course(student_list)}")
print(f"Средняя оценка за лекции: {average_rating_for_course(lecturer_list)}")
