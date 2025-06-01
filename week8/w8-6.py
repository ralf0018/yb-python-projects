class Person(): # Parrent class

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduce(self):
    return f"Hello, my name is {self.name} and I am {self.age} years old."
  
class Student(Person):  # Child class inheriting from Person
  
  def __init__(self, name, age, student_id):
    super().__init__(name, age)  # Call the constructor of the parent class
    self.student_id = student_id # New attribute

  def introduce(self):
    return f"{super().introduce()} My student ID is {self.student_id}."
  
if __name__ == "__main__":
  student = Student('John', 20, '1234')
  print(student.introduce())  
