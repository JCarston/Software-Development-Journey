class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class. This can be named anything you want.

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print(f"Hello my name is {abc.name} {abc.age}")

p1 = Person("John", 36)
p1.myfunc()

#You can also delete attributes from classes using the del keyword. You can apply this to objects as well.
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print(f"Hello my name is {abc.name} {abc.age}")

p1 = Person("John", 36)
# del p1.age
# p1.myfunc()
del p1
p1.myfunc()
