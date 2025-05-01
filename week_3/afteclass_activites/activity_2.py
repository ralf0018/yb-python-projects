class studentsGradingSystem:
  # Constructor to initialize an empty dictionary, ready to store students and their grades
  def __init__(self):
    self.students = {}

  # Method to add a student and the grades
  def addGrades(self, student_name, student_grades):
    if student_name in self.students:
      # if the students already exists, then add grades to the student's grade list
      self.students[student_name].extend(student_grades)
    else:
      # if the student does not exist, then add the student and the grads to the dictionary
      self.students[student_name] = student_grades
    print(f"{student_name} and {student_grades} are added")

  def showResults(self):
    if len(self.students) == 0:
      # Show a message if there is no record
      print("Student grades not recorded")
    else:
      # output all the students and their grades
      print("Here are the students grades:")
      for name, grades in self.students.items():
        print(f"{name} : {grades}")


# a test of studentGradingSystem class
if __name__ == "__main__":
  sys = studentsGradingSystem()
  sys.showResults()
  sys.addGrades("Ada",[80])
  sys.showResults()
  sys.addGrades("Ada",[90])
  sys.showResults()
  sys.addGrades("Bob",[87,91,79])
  sys.showResults()
  