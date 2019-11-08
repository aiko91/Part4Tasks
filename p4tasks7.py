class Student:
    def __init__(self, full_name, age, work):
        self.full_name = full_name
        self.age = age
        self.work = work

    def __str__(self):
        return f'<name: {self.full_name}, age: {self.age}, work: {self.work}>'


rm = Student('Kim Namjoon', 25, 'IDOL')
print(rm)