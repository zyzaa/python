class Student(object):
    def __init__(self, id, name, sex):
        self.id = id
        self.name = name
        self.sex = sex

    def __str__(self):
        return f"{self.id},{self.name},{self.sex}"