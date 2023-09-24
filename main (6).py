class Students:
  
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa=cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student:student.cgpa, reverse=True)
  return sorted_students                   
students = [  
    Students("Indhu", "22B8", 9.1),
    Students("Subi", "22B9", 9.4),
    Students("Sathi", "22B10", 9.0),
    Students("Tamil", "22M34", 9.9),
]
sorted_students = sort_students(students)
for student in sorted_students :
  print("Name:{},Rol Number: {},CGPA:{}".format(student.name,student.roll_number, student.cgpa))
           



