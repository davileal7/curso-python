class Developer(object):
    def __int__(self, skills):
        self.skills = skills

    def __init__(self,other):
        skills = self.skills + other.skills
        return Developer(skills)

def __str__(self):
        return "Skills"

A = Developer('NodeJS')
B = Developer('Python')