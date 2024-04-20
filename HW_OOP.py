# Функция считает среднее значение всех значений словаря
def average_counting(dict_x):  
  all_ratings = []
  for i in list(dict_x.values()):
    all_ratings += i
  average_number = round(sum(all_ratings) / len(all_ratings), 1)
  return average_number

class Mentor: 
  
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []

class Lecturer(Mentor):
  
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.rating = {}

  def __str__(self):
    average_rating = average_counting(self.rating)
    output_string = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rating}'
    return output_string

# Возможность сравнивать лекторов по оценкам
  def __lt__(self, other):
    return(average_counting(self.rating) < average_counting(other.rating))
  def __le__(self, other):
    return(average_counting(self.rating) <= average_counting(other.rating))
  def __eq__(self, other):
    return(average_counting(self.rating) == average_counting(other.rating))
  def __ne__(self, other):
    return(average_counting(self.rating) != average_counting(other.rating))
  def __gt__(self, other):
    return(average_counting(self.rating) > average_counting(other.rating))
  def __ge__(self, other):
   return(average_counting(self.rating) >= average_counting(other.rating))

class Student:  
  
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
  
  def __str__(self):
    average_grades = average_counting(self.grades)
    courses_1 = ', '.join(self.courses_in_progress)
    courses_2 = ', '.join(self.finished_courses)
    output_string = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grades}\nКурсы в процессе изучения: {courses_1}\nЗавершенные курсы: {courses_2}'
    return output_string

  def rate_lecturer(self, lecturer, course, rating):
    if isinstance(lecturer, Lecturer) and ((course in self.finished_courses) or (course in self.courses_in_progress)) and course in lecturer.courses_attached:
      if rating not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        return 'Ошибка, выберите оценку по 10-бальной шкале'
      else:
        pass
      if course in lecturer.rating:
        lecturer.rating[course] += [rating]
      else:
        lecturer.rating[course] = [rating]
    else:
      return 'Ошибка'

# Возможность сравнивать студентов по оценкам
  def __lt__(self, other):
    return(average_counting(self.grades) < average_counting(other.grades))
  def __le__(self, other):
    return(average_counting(self.grades) <= average_counting(other.grades))
  def __eq__(self, other):
    return(average_counting(self.grades) == average_counting(other.grades))
  def __ne__(self, other):
    return(average_counting(self.grades) != average_counting(other.grades))
  def __gt__(self, other):
    return(average_counting(self.grades) > average_counting(other.grades))
  def __ge__(self, other):
    return(average_counting(self.grades) >= average_counting(other.grades))

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
    output_string = f'Имя: {self.name}\nФамилия: {self.surname}'
    return output_string


lecturer_1 = Lecturer('John', 'Doe')
lecturer_1.courses_attached = ['Python', 'PHP', 'C++']
lecturer_2 = Lecturer('Kate', 'Baggings')
lecturer_2.courses_attached = ['Python', 'PHP', 'Pascal']

student_1 = Student('Вася', 'Пупкин', 'муж')
student_1.finished_courses = ['Python', 'C++']
student_1.courses_in_progress = ['PHP', 'Ruby']
student_2 = Student('Иванна', 'Иванова', 'жен')
student_2.finished_courses = ['Python', 'PHP']
student_2.courses_in_progress = ['Pascal', 'Ruby']

reviewer_1 = Reviewer('John', 'Smith')
reviewer_1.courses_attached = ['Python', 'PHP', 'C++', 'Ruby']
reviewer_2 = Reviewer('Jane', 'Smith')
reviewer_2.courses_attached = ['Python', 'PHP', 'Pascal', 'Ruby']

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'PHP', 4)
student_1.rate_lecturer(lecturer_1, 'C++', 3)
student_2.rate_lecturer(lecturer_1, 'Python', 7)
student_2.rate_lecturer(lecturer_2, 'PHP', 8)
student_2.rate_lecturer(lecturer_2, 'Pascal', 10)

reviewer_1.rate_hw(student_1, 'PHP', 3)
reviewer_1.rate_hw(student_1, 'Ruby', 4)
reviewer_2.rate_hw(student_2, 'Pascal', 7)
reviewer_2.rate_hw(student_2, 'Ruby', 7)

print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)
print(reviewer_1)
print(reviewer_2)

print(lecturer_2 < lecturer_1)
print(student_1 != student_2)

# Ниже функция для счета средних оценок за дз и лекций

def average_hw_course(students, course):
  total_hw = []
  for i in students:
    if course in i.grades.keys():
      total_hw += i.grades[course]
    else:
      pass
  return (round(sum(total_hw) / len(total_hw), 1))

def average_lecturer_rating_course(lecturers, course):
  total_rating = []
  for i in lecturers:
    if course in i.rating.keys():
      total_rating += i.rating[course]
    else:
      pass
  return (round(sum(total_rating) / len(total_rating), 1))